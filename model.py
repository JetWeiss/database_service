from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config import Base, Base2


class Batch(Base, Base2):
    __tablename__ = "batches"
    __table_args__ = {"schema": "lvl1trs"}
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
    __table_args__ = {"schema": "lvl1trs"}
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
    __table_args__ = {"schema": "lvl1trs"}
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
    __table_args__ = {"schema": "lvl1trs"}
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
    __table_args__ = {"schema": "lvl1trs"}
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
    __table_args__ = {"schema": "lvl1trs"}
    id = Column(Integer)
    transactionUuid = Column(String, primary_key=True)
    vehicleUuid = Column(String)
    operatorId = Column(Integer)
    turnUuid = Column(String)
    lastCountry = Column(Integer)
    lastSociety = Column(Integer)
    lastNetwork = Column(Integer)
    lastPlaza = Column(Integer)
    lastLane = Column(Integer)
    lastPayDt = Column(DateTime)
    country = Column(Integer)
    society = Column(Integer)
    plaza = Column(Integer)
    lane = Column(Integer)
    entryDt = Column(DateTime)
    entryClass = Column(Integer)
    addVehicleBy = Column(String)
    setClassDt = Column(DateTime)
    vehicleClass = Column(Integer)
    setVehicleClassBy = Column(String)
    exitDt = Column(DateTime)
    exitClass = Column(Integer)
    deleteVehicleBy = Column(String)
    beginPayDt = Column(DateTime)
    endPayDt = Column(DateTime)
    payType = Column(Integer)
    payDevice = Column(String)
    fareModulation = Column(Integer)
    fareType = Column(Integer)
    fare = Column(Integer)
    balanceBefore = Column(Integer)
    balanceAfter = Column(Integer)
    banknoteNominal = Column(Integer)
    banknoteNumber = Column(String)
    pan = Column(String)
    payCode = Column(Integer)
    terminalId = Column(String)
    authCode = Column(String)
    ocrPlate = Column(String)
    transactionCompleted = Column(Integer)
    ocrCountry = Column(String)
    transitCode = Column(String)
    receiptNumber = Column(String)
    lastPayType = Column(Integer)
    fareId = Column(Integer)
    writeReceiptDt = Column(DateTime)
    lastWriteReceiptDt = Column(DateTime)
    ocrPlateBack = Column(String)
    ocrCountryBack = Column(String)
    vehicleCategory = Column(Integer)
    vatAmount = Column(Integer)
    transactionNumber = Column(Integer)
    ocrPlateReliability = Column(Integer)
    receiptOrder = Column(Integer)
    payToolOrder = Column(Integer)
    tableVersion = Column(Integer, primary_key=True)
    def __init__(self, id, transactionUuid, vehicleUuid, operatorId, turnUuid, lastCountry, lastSociety, lastNetwork,
                 lastPlaza, lastLane, lastPayDt, country, society, plaza, lane, entryDt, entryClass, addVehicleBy,
                 setClassDt, vehicleClass, setVehicleClassBy, exitDt, exitClass, deleteVehicleBy, beginPayDt, endPayDt,
                 payType, payDevice, fareModulation, fareType, fare, balanceBefore, balanceAfter, banknoteNominal,
                 banknoteNumber, pan, payCode, terminalId, authCode, ocrPlate, transactionCompleted, ocrCountry,
                 transitCode, receiptNumber, lastPayType, fareId, writeReceiptDt, lastWriteReceiptDt, ocrPlateBack,
                 ocrCountryBack, vehicleCategory, vatAmount, transactionNumber, ocrPlateReliability, receiptOrder,
                 payToolOrder, tableVersion):
        self.id = id
        self.transactionUuid = transactionUuid
        self.vehicleUuid = vehicleUuid
        self.operatorId = operatorId
        self.turnUuid = turnUuid
        self.lastCountry = lastCountry
        self.lastSociety = lastSociety
        self.lastNetwork = lastNetwork
        self.lastPlaza = lastPlaza
        self.lastLane = lastLane
        self.lastPayDt = lastPayDt
        self.country = country
        self.society = society
        self.plaza = plaza
        self.lane = lane
        self.entryDt = entryDt
        self.entryClass = entryClass
        self.addVehicleBy = addVehicleBy
        self.setClassDt = setClassDt
        self.vehicleClass = vehicleClass
        self.setVehicleClassBy = setVehicleClassBy
        self.exitDt = exitDt
        self.exitClass = exitClass
        self.deleteVehicleBy = deleteVehicleBy
        self.beginPayDt = beginPayDt
        self.endPayDt = endPayDt
        self.payType = payType
        self.payDevice = payDevice
        self.fareModulation = fareModulation
        self.fareType = fareType
        self.fare = fare
        self.balanceBefore = balanceBefore
        self.balanceAfter = balanceAfter
        self.banknoteNominal = banknoteNominal
        self.banknoteNumber = banknoteNumber
        self.pan = pan
        self.payCode = payCode
        self.terminalId = terminalId
        self.authCode = authCode
        self.ocrPlate = ocrPlate
        self.transactionCompleted = transactionCompleted
        self.ocrCountry = ocrCountry
        self.transitCode = transitCode
        self.receiptNumber = receiptNumber
        self.lastPayType = lastPayType
        self.fareId = fareId
        self.writeReceiptDt =writeReceiptDt
        self.lastWriteReceiptDt = lastWriteReceiptDt
        self.ocrPlateBack = ocrPlateBack
        self.ocrCountryBack = ocrCountryBack
        self.vehicleCategory = vehicleCategory
        self.vatAmount = vatAmount
        self.transactionNumber = transactionNumber
        self.ocrPlateReliability = ocrPlateReliability
        self.receiptOrder = receiptOrder
        self.payToolOrder = payToolOrder
        self.tableVersion = tableVersion

class Employee(Base, Base2):
    __tablename__ = "employees"
    __table_args__ = {"schema": "lvl1trs"}
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
    __table_args__ = {"schema": "lvl1trs"}
    id = Column(String)
    turnUuid = Column(String, primary_key=True)
    operatorId = Column(Integer)
    masterUuid = Column(String)
    profile = Column(String)
    direction = Column(String)
    country = Column(Integer)
    society = Column(Integer)
    network = Column(Integer)
    plaza = Column(Integer)
    lane = Column(Integer)
    laneMode = Column(String)
    state = Column(String)
    beginDt = Column(DateTime)
    endDt = Column(DateTime)
    firstRecptNum = Column(Integer)
    lastRecptNum = Column(Integer)
    laneType = Column(String)
    def __init__(self, id, turnUuid, operatorId, masterUuid, profile, direction, country, society, network, plaza, lane,
                 laneMode, state, beginDt, endDt, firstRecptNum, lastRecptNum, laneType):
        self.id = id
        self.turnUuid = turnUuid
        self.operatorId = operatorId
        self.masterUuid = masterUuid
        self.profile = profile
        self.direction = direction
        self.country = country
        self.society = society
        self.network = network
        self.plaza = plaza
        self.lane = lane
        self.laneMode = laneMode
        self.state = state
        self.beginDt = beginDt
        self.endDt = endDt
        self.firstRecptNum = firstRecptNum
        self.lastRecptNum = lastRecptNum
        self.laneType = laneType

class Client(Base, Base2):
    __tablename__ = "clients"
    __table_args__ = {"schema": "lvl1trs"}
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

