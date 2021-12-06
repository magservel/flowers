from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dataset(Base):
    __tablename__ = "Dataset"
    data_id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    train = Column(Boolean)
