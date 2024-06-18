from models.contracts import Contract
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def get_contract_by_id(db: AsyncSession, contract_id: int) -> Contract | None:
    result = await db.execute(select(Contract).where(Contract.id == contract_id))
    return result.scalars().first()
