from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import TypeDecorator
from datetime import datetime
import json

# Custom JSON Type
class JSONEncodedText(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)  # Serialize to JSON string
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)  # Deserialize back to Python object
        return value

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
    main_store = Column(String, nullable=False)

class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    full_name = Column(Text, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String(15), nullable=False)  # Changed to String for phone numbers
    company_name = Column(Text, nullable=False)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class Buyer(Base):
    __tablename__ = 'buyers'  # Lowercased table name for consistency

    id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String(15), nullable=False)  # Changed to String for phone numbers
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

if __name__ == "__main__":
    # Create all tables
    Base.metadata.create_all(bind=engine)
