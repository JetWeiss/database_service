from config import loadSession1, loadSession2
from model import Batch, Change, Channel, Client_group, Table_info, Transaction, Employee, Turn, Client
from threading import Thread, Event
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import time
from sqlalchemy.sql import and_

event = Event()

def PauseOrEnabled(session1, session2, change_b):
    tables_info1 = session1.query(Table_info).filter(Table_info.table_name == change_b.src_table_name).first()
    tables_info2 = session2.query(Table_info).filter(Table_info.table_name == change_b.src_table_name).first()
    client_ch1 = session1.query(Client).filter(Client.group_id == tables_info1.group_id).first()
    client_ch2 = session2.query(Client).filter(Client.group_id == tables_info2.group_id).first()
    client_gr1 = session1.query(Client_group).filter(Client_group.group_id == tables_info1.group_id).first()
    client_gr2 = session2.query(Client_group).filter(Client_group.group_id == tables_info2.group_id).first()
    channel_ch1 = session1.query(Channel).filter(Channel.channel_id == change_b.src_table_name).first()
    channel_ch2 = session2.query(Channel).filter(Channel.channel_id == change_b.src_table_name).first()
    if (client_ch1.enabled == True and client_ch1.paused == False) \
            and (client_ch2.enabled == True and client_ch2.paused == False) \
            and (client_gr1.enabled == True and client_gr1.paused == False) \
            and (client_gr2.enabled == True and client_gr2.paused == False) \
            and (tables_info1.enabled == True and tables_info1.paused == False) \
            and (tables_info2.enabled == True and tables_info2.paused == False) \
            and (channel_ch1.enabled == True and channel_ch1.paused == False) \
            and (channel_ch2.enabled == True and channel_ch2.paused == False):
        return True
    else:
        return False

def StatusRecord(batch, status_b, session):
    batch.batch_status = status_b
    session.commit()

def MakeChanges(modified_string, batch, Trans_IU, Truns_D, session1, session2):
    if modified_string.event_type == 'I' or modified_string.event_type == 'U':
        try:
            session2.add(Trans_IU)
            session2.flush()
            session2.commit()
            print('I')
        except (SQLAlchemyError or RuntimeError) as e:
            batch.error_string = 'Error inserting transaction: {error}'.format(error=e)
            batch.batch_status = 'E'
            session1.commit()
    elif modified_string.event_type == 'D':
        try:
            if Truns_D != None:
                Truns_D.delete()
            session2.flush()
            session2.commit()
            print('D')
        except (SQLAlchemyError or RuntimeError) as e:
            batch.error_string = 'Error deleting transaction: {error}'.format(error=e)
            batch.batch_status = 'E'
            session1.commit()

def SearchChanges(session1, session2):
    while True:
        event.wait()
        new_batch = None
        Trans_IU = None
        Truns_D = None
        Change_table = None
        primary_key_t = None
        primary_key_v = None
        while new_batch == None:
            new_batch = session1.query(Batch).filter(Batch.batch_status == "N").first()
            if new_batch == None:
                time.sleep(10)
        new_batch.start_process_dt = 'now()'
        StatusRecord(new_batch, 'L', session1)
        start_time = datetime.now()
        co_batches = 0
        while co_batches < new_batch.batch_record_count:
            change_b = None
            change_b = session1.query(Change).filter(Change.batch_id == new_batch.batch_id).offset(co_batches).limit(1).all()
            co_batches += 1
            if change_b[0].src_table_name == 'transactions':
                Change_table = Transaction
                primary_key_t = Change_table.transactionUuid
                primary_key_v = Change_table.tableVersion
            elif change_b[0].src_table_name == 'employees':
                Change_table = Employee
                primary_key_t = Change_table.insurance_id
            elif change_b[0].src_table_name == 'turns':
                Change_table = Turn
                primary_key_t = Change_table.turnUuid
            if change_b[0].event_type != 'D':
                if change_b[0].src_table_name == 'transactions':
                    Trans_up = session1.query(Change_table).filter(
                        and_(primary_key_v == change_b[0].pk_column_values[1],
                             primary_key_t == change_b[0].pk_column_values[0])).limit(1).all()
                else:
                    Trans_up = session1.query(Change_table).filter(
                        primary_key_t == change_b[0].pk_column_values[0]).limit(1).all()
                Trans_IU = session2.merge(Trans_up[0])
            else:
                if change_b[0].src_table_name == 'transactions':
                    Truns_D = session2.query(Change_table).filter(
                        and_(primary_key_v == change_b[0].pk_column_values[1],
                             primary_key_t == change_b[0].pk_column_values[0]))
                else:
                    Truns_D = session2.query(Change_table).filter(
                        primary_key_t == change_b[0].pk_column_values[0])
            new_batch.start_send_dt = 'now()'
            StatusRecord(new_batch, 'S', session1)
            while PauseOrEnabled(session1, session2, change_b[0]) == False:
                time.sleep(5)
            MakeChanges(change_b[0], new_batch, Trans_IU, Truns_D, session1, session2)
            # if change_b.src_table_name == 'transactions':
            #     miss_c = None
            #     while miss_c == None:
            #         miss_c = session2.query(Batch).filter(Batch.batch_id > new_batch.batch_id).first()
            #         if miss_c == None:
            #             time.sleep(1)
            #     miss_c.batch_status = 'C'
            #     session2.commit()
        end_time = datetime.now() - start_time
        new_batch.process_time = end_time
        new_batch.end_process_dt = 'now()'
        StatusRecord(new_batch, 'C', session1)


if __name__ == "__main__":
    event.clear()
    ses1 = loadSession1()
    ses2 = loadSession2()
    t1 = Thread(target=SearchChanges, args=(ses1, ses2)).start()
    t2 = Thread(target=SearchChanges, args=(ses2, ses1)).start()
    ses1.close()
    ses2.close()
    event.set()

