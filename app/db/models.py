from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True, nullable=False)
    chunk_strategy = Column(String, default="default", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    interview_date = Column(String, nullable=False)   # store as string or use Date column
    interview_time = Column(String, nullable=False)   # store as string
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
