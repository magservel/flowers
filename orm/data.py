from sqlalchemy import create_engine, Column, Integer, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
import pandas as pd

Base = declarative_base()


class Dataset(Base):
    __tablename__ = "Dataset"
    data_id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    train = Column(Boolean)


def get_dataset(train=True):
    engine = create_engine("sqlite:///sql/data.db")
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    data = pd.read_sql(s.query(Dataset).with_entities(Dataset.x, Dataset.y).filter(Dataset.train == train).statement,
                       s.bind)

    s.close()
    return data


def add_data(x, y, train):
    engine = create_engine("sqlite:///sql/data.db")
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    data = Dataset(x=x, y=y, train=train)
    s.add(data)

    s.commit()
    s.close()


def populate_db():
    engine = create_engine("sqlite:///sql/data.db")
    Base.metadata.create_all(engine)

    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "./data/train.csv"

        with open(file_name, 'r') as file:
            data = csv.DictReader(file)

            for d in data:
                if d['x'] is not None and d['y'] is not None:
                    entry = Dataset(**{
                        'x': float(d['x']),
                        'y': float(d['y']),
                        'train': True
                    })

                    s.add(entry)

        file_name = "./data/test.csv"
        with open(file_name, 'r') as file:
            data = csv.DictReader(file)
            for d in data:
                if d['x'] is not None and d['y'] is not None:
                    entry = Dataset(**{
                        'x': float(d['x']),
                        'y': float(d['y']),
                        'train': False
                    })
                    s.add(entry)

        s.commit()
    except Exception as e:
        s.rollback()
    finally:
        s.close()


if __name__ == "__main__":
    pass
