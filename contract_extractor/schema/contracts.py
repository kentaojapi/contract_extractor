from pydantic import BaseModel, Field
from schema_for_llm.data_in_contract import DataInContract


class ContractBase(BaseModel):
    id: int
    name: str = Field(..., example="contract.pdf")

    class Config:
        from_attributes = True
        orm_mode = True


class ContractRegisterRequest(ContractBase): ...


class ContractDetailResponse(ContractBase, DataInContract): ...
