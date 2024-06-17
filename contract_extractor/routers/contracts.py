from fastapi import APIRouter

router = APIRouter()


@router.get("/contaracts")
def get_all_constracts() -> None: ...


@router.post("/contracts")
def register_constarct() -> None: ...


@router.get("/contracts/{constract_id}/details")
def get_contract_details() -> None: ...
