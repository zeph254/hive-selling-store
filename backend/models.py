from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database engine
engine = create_engine("sqlite:///Hive.db", echo=True)

# Session factory
Session = sessionmaker(bind=engine)

# Dependency to get the database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Base for ORM models
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(Text, nullable=False)
    product_price = Column(Integer, nullable=False)
    product_type = Column(Text, nullable=False)
    main_store = Column(VARCHAR, nullable=False)

class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    full_name = Column(Text, nullable=False)
    email = Column(VARCHAR, nullable=False)
    phone_number = Column(Integer, nullable=False)
    company_name = Column(Text, nullable=False)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Buyer(Base):
    __tablename__ = 'Buyers'

    id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    email = Column(VARCHAR, nullable=False)
    phone_number = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

if __name__ == "__main__":
    # Create all tables
    Base.metadata.create_all(bind=engine)

