from config import loadSession1, loadSession2
from model import Batch, Change, Channel, Client_group, Table_info, Transaction, Employee, Turn, Client
from threading import Thread, Event
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import time

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
    if (client_ch1.enabled == True and client_ch1.paused == False) and (client_ch2.enabled == True and client_ch2.paused == False)\
        and (client_gr1.enabled == True and client_gr1.paused == False) and (client_gr2.enabled == True and client_gr2.paused == False) \
            and (tables_info1.enabled == True and tables_info1.paused == False) and (tables_info2.enabled == True and tables_info2.paused == False) \
                and (channel_ch1.enabled == True and channel_ch1.paused == False) and (channel_ch2.enabled == True and channel_ch2.paused == False):
        return True
    else:
        return False

def SearchChanges(session1, session2):
    while True:
        event.wait()
        res = None
        Trans_in = None
        Change_table = None
        primary_key_t = None
        while res == None:
                res = session1.query(Batch).filter(Batch.batch_status == "N").first()
                if res == None:
                    time.sleep(10)
        res.start_process_dt = 'now()'
        res.batch_status = 'L'
        session1.commit()
        start_time = datetime.now()
        for i in range(0, res.batch_record_count):
            change_b = session1.query(Change).filter(Change.batch_id == res.batch_id).offset(i).first()
            if change_b.src_table_name == 'transactions':
                Change_table = Transaction
                primary_key_t = Change_table.transaction_id
            elif change_b.src_table_name == 'employees':
                Change_table = Employee
                primary_key_t = Change_table.insurance_id
            elif change_b.src_table_name == 'turns':
                Change_table = Turn
                primary_key_t = Change_table.turn_id
            if change_b.pk_column_values[1] != '2':
                Trans_up = session1.query(Change_table).filter(primary_key_t == change_b.pk_column_values[0]).first()
                Trans_in = session2.merge(Trans_up)
            res.start_send_dt = 'now()'
            res.batch_status = 'S'
            session1.commit()
            while PauseOrEnabled(session1, session2, change_b) == False:
                time.sleep(5)
            if change_b.event_type == 'I':
                try:
                    print('I')
                    session2.add(Trans_in)
                    session2.commit()
                except (SQLAlchemyError or RuntimeError) as e:
                    res.error_string = 'Error inserting transaction: {error}'.format(error=e)
                    res.batch_status = 'E'
                    session1.commit()
            elif change_b.event_type == 'U':
                try:
                    print('U')
                    Trans_ch = session2.query(Change_table).filter(primary_key_t == change_b.pk_column_values[0]).first()
                    Trans_ch = Trans_in
                    session2.commit()
                except (SQLAlchemyError or RuntimeError) as e:
                    res.error_string = 'Error updating transaction: {error}'.format(error=e)
                    res.batch_status = 'E'
                    session1.commit()
            elif change_b.event_type == 'D':
                try:
                    print('D')
                    Trans_ch = session2.query(Change_table).filter(primary_key_t == change_b.pk_column_values[0])
                    Trans_ch.delete()
                    session2.commit()
                except (SQLAlchemyError or RuntimeError) as e:
                    res.error_string = 'Error deleting transaction: {error}'.format(error=e)
                    res.batch_status = 'E'
                    session1.commit()
            if change_b.src_table_name == 'transactions':
                miss_c = None
                while miss_c == None:
                    miss_c = session2.query(Batch).filter(Batch.batch_id > res.batch_id).first()
                    if miss_c == None:
                        time.sleep(1)
                miss_c.batch_status = 'C'
                session2.commit()
        end_time = datetime.now() - start_time
        res.process_time = end_time
        res.end_process_dt = 'now()'
        res.batch_status = 'C'
        session1.commit()

if __name__ == "__main__":
    event.clear()
    ses1 = loadSession1()
    ses2 = loadSession2()
    t1 = Thread(target=SearchChanges, args=(ses1, ses2)).start()
    t2 = Thread(target=SearchChanges, args=(ses2, ses1)).start()
    ses1.close()
    ses2.close()
    event.set()

