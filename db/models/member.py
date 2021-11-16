from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from db.config import Base

class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('team.id'), nullable=False)