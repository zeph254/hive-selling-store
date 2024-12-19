from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Text, DateTime, ForeignKey

Base = declarative_base()

class product(Base):
    __tablename__  = 'products'

    id = Column(Integer(), primary_key=True)
    Product_name = Column(Text(),nullable=False)
    Product_price = Column(Integer(),nullable=False)
    Product_type = Column(Text(), nullable=False)
    main_store = Column(VARCHAR,nullable=False)


class seller(Base):
     __tablename__ = 'sellers'  

     id = Column(Integer(), primary_key=True) 
     product_id = Column(Integer(),ForeignKey("products.id"),nullable=False)
     full_name = Column(Text(),nullable=False) 
     email = Column(VARCHAR,nullable=False)
     phone_number = Column(Integer(),nullable=False) 
     company_name = Column(Text(),nullable=False)
     address = Column(Text(),nullable=True)
     created_at = Column(DateTime(),nullable=False)

