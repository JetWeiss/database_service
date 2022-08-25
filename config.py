from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://server1:server1@192.168.56.101/server1')
engine2 = create_engine('postgresql://server2:server2@192.168.56.102/server2')
Base = declarative_base(engine)
Base2 = declarative_base(engine2)


def loadSession1():
    metadata = Base.metadata
    Session1 = sessionmaker(bind=engine)
    session1 = Session1()
    return session1

def loadSession2():
    metadata = Base2.metadata
    Session2 = sessionmaker(bind=engine2)
    session2 = Session2()
    return session2