from typing import List
# from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from Model.supplier import Vendors


class SupplierDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_all_suppliers(self) -> List[Vendors]:
        q = await self.db_session.execute(select(Vendors).order_by(Vendors.vendor_id))
        return q.scalars().all()