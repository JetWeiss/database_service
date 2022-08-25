from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config import Base, Base2


class Batch(Base, Base2):
    __tablename__ = "batches"
    batch_id = Column(Integer, primary_key=True)
    client_id = Column(String)
    batch_status = Column(String)
    batch_record_count = Column(Integer)
    process_time = Column(DateTime)
    start_process_dt = Column(DateTime)
    start_send_dt = Column(DateTime)
    end_process_dt = Column(DateTime)
    error_string = Column(String)
    insert_dt = Column(DateTime)
    def __init__(self, batch_id, client_id, batch_status, batch_record_count, process_time, start_process_dt, start_send_dt, end_process_dt, error_string, insert_dt):
        self.batch_id = batch_id
        self.client_id = client_id
        self.batch_status = batch_status
        self.batch_record_count = batch_record_count
        self.process_time = process_time
        self.start_process_dt = start_process_dt
        self.start_send_dt = start_send_dt
        self.end_process_dt = end_process_dt
        self.error_string = error_string
        self.insert_dt = insert_dt

class Change(Base, Base2):
    __tablename__ = "changes"
    batch_id = Column(Integer, primary_key=True)
    src_table_name = Column(String)
    dst_table_name = Column(String)
    pk_column_names = Column(String)
    pk_column_values = Column(String)
    event_type = Column(String)
    insert_dt = Column(DateTime)
    def __init__(self, batch_id, src_table_name, dst_table_name, pk_column_names, pk_column_values, event_type, insert_dt):
        self.batch_id = batch_id
        self.src_table_name = src_table_name
        self.dst_table_name = dst_table_name
        self.pk_column_names = pk_column_names
        self.pk_column_values = pk_column_values
        self.event_type = event_type
        self.insert_dt = insert_dt

class Channel(Base, Base2):
    __tablename__ = "channels"
    channel_id = Column(String, primary_key=True)
    max_count_to_send = Column(Integer)
    enabled = Column(Boolean)
    paused = Column(Boolean)
    insert_dt = Column(DateTime)
    def __init__(self, channel_id, max_count_to_send, enabled, paused, insert_dt):
        self.channel_id = channel_id
        self.max_count_to_send = max_count_to_send
        self.enabled = enabled
        self.paused = paused
        self.insert_dt = insert_dt

class Client_group(Base, Base2):
    __tablename__ = "clients_groups"
    group_id = Column(String, primary_key=True)
    group_type = Column(String)
    enabled = Column(Boolean)
    paused = Column(Boolean)
    insert_dt = Column(DateTime)
    def __init__(self, group_id, group_type, enabled, paused, insert_dt):
        self.group_id = group_id
        self.group_type = group_type
        self.enabled = enabled
        self.paused = paused
        self.insert_dt = insert_dt

class Table_info(Base, Base2):
    __tablename__ = "tables_info"
    table_name = Column(String, primary_key=True)
    dst_table_name = Column(String)
    group_id = Column(String)
    data_moved_type = Column(String)
    channel_id = Column(String)
    enabled = Column(Boolean)
    paused = Column(Boolean)
    insert_dt = Column(DateTime)
    def __init__(self, table_name, dst_table_name, group_id, data_maved_type, channel_id, enabled, paused, insert_dt):
        self.table_name = table_name
        self.dst_table_name = dst_table_name
        self.group_id = group_id
        self.data_moved_type = data_maved_type
        self.channel_id = channel_id
        self.enabled = enabled
        self.paused = paused
        self.insert_dt = insert_dt

class Transaction(Base, Base2):
    __tablename__ = "transactions"
    transaction_id = Column(String, primary_key=True)
    plazaId = Column(String)
    laneId = Column(String)
    countryId = Column(String)
    ticketNumber = Column(String)
    def __init__(self, transaction_id, plazaId, laneId, countryId, ticketNumber):
        self.transaction_id = transaction_id
        self.plazaId = plazaId
        self.laneId = laneId
        self.countryId = countryId
        self.ticketNumber = ticketNumber

class Employee(Base, Base2):
    __tablename__ = "employees"
    insurance_id = Column(String, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    position = Column(String)
    current = Column(Boolean)
    def __init__(self, insurance_id, f_name, l_name, position, current):
        self.insurance_id = insurance_id
        self.f_name = f_name
        self.l_name = l_name
        self.position = position
        self.current = current

class Turn(Base, Base2):
    __tablename__ = "turns"
    turn_id = Column(String, primary_key=True)
    laneId = Column(String)
    count = Column(String)
    enabled = Column(Boolean)
    def __init__(self, turn_id, laneId, count, enabled):
        self.turn_id = turn_id
        self.laneId = laneId
        self.count = count
        self.enabled = enabled

class Client(Base, Base2):
    __tablename__ = "clients"
    client_id = Column(String, primary_key=True)
    group_id = Column(String)
    client_host = Column(String)
    enabled = Column(Boolean)
    paused = Column(Boolean)
    insert_dt = Column(DateTime)

    def __init__(self, client_id, group_id, client_host, enabled, paused, insert_dt):
        self.client_id = client_id
        self.group_id = group_id
        self.client_host = client_host
        self.enabled = enabled
        self.paused = paused
        self.insert_dt = insert_dt

