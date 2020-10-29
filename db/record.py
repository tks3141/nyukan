import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Interval
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from setting import Base
from setting import ENGINE
from user import User
    
class Record(Base):
    """
    ユーザーの入退館履歴
    """
    __tablename__ = 'records'
    id = Column('id', Integer, primary_key = True,autoincrement=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    
    login = Column(DateTime)
    logout = Column(DateTime)
    stayed_time = Column(Interval)

    user = relationship("User")

    def interval(self):
        print(self.login)
        # if(self.login and self.logout)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
