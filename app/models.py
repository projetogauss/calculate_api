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

    def somar(self, arq1, arq2):       
        try:
            result = arq1 + arq2
        except:
            raise
        return result

    def dividir(self, arq1, arq2):
        if arq2 > 0:
            result = arq1 / arq2
        else:
            print("Divisão por 0 escolha outro valor")
        return result
    
    def multiplicar(self, arq1, arq2):
        try:
            result = arq1 * arq2
        except:
            raise
        return result
    
    def subtrair(self, arq1, arg2):
        try:
            result = arq1 - arg2
        except:
            raise
        return result
