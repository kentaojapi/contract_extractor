from db import Base
from sqlalchemy import Column, Integer, String


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024), nullable=False)
