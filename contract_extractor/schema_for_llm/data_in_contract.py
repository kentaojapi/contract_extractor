from typing import Literal

from pydantic import BaseModel, Field


class Address(BaseModel):
    prefecture: str = Field(description="prefecture（県）")
    city: str = Field(description="city（市区）")
    town: str = Field(description="town（町村）")
    street: str = Field(description="steet number")


class Company(BaseModel):
    name: str = Field(description="Name of the company.")
    role: Literal["customer", "provider"] = Field(
        description="Role of the company. customer or provider."
    )
    address: Address = Field(description="Address of the company.")


class ContractTerm(BaseModel):
    start_date: str = Field(
        description="Start date of the contract period. The format is YYYY-MM-DD"
    )
    end_date: str = Field(
        description="End date of the contract period. The format is YYYY-MM-DD"
    )


class DataInContract(BaseModel):
    document_title: str = Field(description="Title of the contract.")
    companies: list[Company] = Field(
        description="Companies mentioned within the contract"
    )
    contract_term: ContractTerm = Field(description="Term of Contract.")
