from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Text, DateTime

Base = declarative_base()

class product(Base):
    __tablename__  = 'products'

    id = Column(Integer(), primary_key=True)
    Product_name = Column(Text(),nulluble=False)
    Product_price = Column(Integer(),nulluble=False)
    Product_type = Column(VARCHAR,nullable=True)
    main_store = Column(VARCHAR,nulluble=False)

