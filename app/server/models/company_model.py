from pydantic import BaseModel

class CompanyModel(BaseModel):
    id : int
    name: str
    CNPJ: int
    products: list[dict]
    