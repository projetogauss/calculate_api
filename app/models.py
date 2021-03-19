from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price : float
    juros : float
    tax : Optional[float] = None
    acao : str
    result : Optional[float] = None

