#!/usr/bin/python
from sqlalchemy import Column, Integer, String
from Config.config import Base


class Vendors(Base):
    __tablename__ = 'vendors'

    vendor_id = Column(Integer, primary_key=True, nullable=False)
    vendor_name = Column(String, nullable=False)
    