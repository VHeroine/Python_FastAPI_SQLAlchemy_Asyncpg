
from fastapi import FastAPI
from typing import List
from Model.supplier import Vendors
from Dal.vendors import SupplierDAL
from Config.config import async_session


app = FastAPI()

@app.get("/api/vendors", status_code=200)
async def get_all_vendors() -> List[Vendors]:
    async with async_session() as session:
        async with session.begin():
            supplier_dal = SupplierDAL(session)
            return await supplier_dal.get_all_vendors()

@app.post("/api/vendors", status_code=204)
async def create_vendor(vendor_name: str):
    async with async_session() as session:
        async with session.begin():
            supplier_dal = SupplierDAL(session)
            return await supplier_dal.create_vendor(vendor_name)
