from sqlmodel import SQLModel, create_engine
from sqlmodel import Session as SQLModelSession 
from app.models import Product
from sqlmodel import select

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"
DATABASE_URL = "sqlite:///./db.sqlite3"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=SQLModelSession  # これが重要！
)

def get_db():
    db = SQLModelSession(engine)
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def populate_sample_products():
    products = [
        Product(name="フレンチトースト石鹸", price=1200, description="食べられません"),
        Product(name="レトロ電話型タイマー", price=1980, description="おしゃれなキッチンの友"),
        Product(name="猫耳Bluetoothスピーカー", price=4980, description="猫派必携のアイテム！"),
    ]

    with SQLModelSession(engine) as session:
        if session.exec(select(Product)).first():
            return  # すでにデータがあればスキップ
        session.add_all(products)
        session.commit()
