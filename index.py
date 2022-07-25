
from fastapi import FastAPI
from typing import List
from Model.supplier import Vendors
from Dal.vendors import SupplierDAL
from Config.config import async_session


app = FastAPI()

@app.get("/api/suppliers", status_code=200)
async def get_all_books() -> List[Vendors]:
    async with async_session() as session:
        async with session.begin():
            supplier_dal = SupplierDAL(session)
            return await supplier_dal.get_all_suppliers()