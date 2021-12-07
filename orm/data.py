from sqlalchemy import create_engine, Column, Integer, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv

Base = declarative_base()


class Dataset(Base):
    __tablename__ = "Dataset"
    data_id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    train = Column(Boolean)


if __name__ == "__main__":
    engine = create_engine("sqlite:///../sql/data.db")
    Base.metadata.create_all(engine)

    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "../data/train.csv"
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

        file_name = "../data/test.csv"
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
