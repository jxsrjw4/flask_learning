from sqlalchemy import Column,Integer,String

from app import db

class Supplier(db.Model):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False)
    area = Column(String(50), nullable= False)
    address = Column(String(100))
    contacter = Column(String(100))
    telephone = Column(String(100))