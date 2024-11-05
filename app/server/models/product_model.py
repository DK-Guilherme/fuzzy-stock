from pydantic import BaseModel, Field
from typing import Annotated

class ProductModel(BaseModel):
    id: Annotated[int, Field(...)]
    name: Annotated[str, Field(max_length=30)]
    price: Annotated[float, Field(max_length=999999)]
    description: Annotated[str, Field(max_digits=150)]
    qtdin_stock: Annotated[int, Field(max_length=999)]
    last_update: Annotated[str, Field(max_digits=10)]
    updated_by: Annotated[str, Field(max_digits=20)]
    created_at: Annotated[str, Field(max_digits=10)]
    