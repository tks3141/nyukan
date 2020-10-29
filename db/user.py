import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from setting import Base
from setting import ENGINE

class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True,autoincrement=True)
    name = Column('name', String(200))
    status = Column('status', Integer)
    slack_id = Column(String(200))
    last_login = Column(Integer)

    idms = relationship("NFC",backref="users")
    
class NFC(Base):
    """
    ゆーざーごとのNFCのIDMモデル 
    """
    __tablename__ = 'idms'
    id = Column('id', Integer, primary_key = True,autoincrement=True)
    users_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"))
    idm = Column('idm', String(16))

    user = relationship("User")

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
