from cruds.contracts import get_contract_by_id
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, Path
from llm_chains.contract_registration import extract_contract_details
from schema.contracts import ContractBase, ContractDetailResponse
from schema_for_llm.data_in_contract import DataInContract
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/contaracts")
def get_all_constracts() -> None: ...


@router.post("/contracts")
def register_constarct() -> None: ...


@router.get("/contracts/{contract_id}/details", response_model=ContractDetailResponse)
async def get_contract_details(
    contract_id: int = Path(...), db: AsyncSession = Depends(get_db)
) -> ContractDetailResponse:
    contract_base_from_orm = await get_contract_by_id(db, contract_id)

    if not contract_base_from_orm:
        raise HTTPException(status_code=404, detail="Contract not found")

    try:
        contract_details = extract_contract_details(contract_base_from_orm.name)
    except:
        raise HTTPException(
            status_code=500, detail="Extraction from pdf file failed"
        ) from None

    contract_base = ContractBase.from_orm(contract_base_from_orm)
    return _merge_contract_attributes(contract_base, contract_details)


def _merge_contract_attributes(
    contract_base: ContractBase, contract_details: DataInContract
) -> ContractDetailResponse:
    contract_full_dict = {**contract_base.dict(), **contract_details.dict()}
    return ContractDetailResponse(**contract_full_dict)
