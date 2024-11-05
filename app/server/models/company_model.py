from pydantic import BaseModel
from typing import Optional, Annotated
class CompanyModel(BaseModel):
    id : int
    name: str
    cnpj: int
    