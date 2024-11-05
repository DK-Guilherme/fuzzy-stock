from pydantic import BaseModel
class CompanyModel(BaseModel):
    id : int
    name: str
    cnpj: int
    