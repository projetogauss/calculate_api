from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import logging


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price : float
    juros : float
    acao : str

    #metedo com a operacao de somar
    def somar(self, arq1, arq2):       
        try:
            result = {"result" : arq1 + arq2}
            json_result = jsonable_encoder(result)
        except:
            raise
        return JSONResponse(content=json_result)

    #metedo com a operacao de dividir
    def dividir(self, arq1, arq2):
        json_result = None
        try:
            result = {"result" : arq1 / arq2}
            json_result = jsonable_encoder(result)
        except ZeroDivisionError as error:
            logging.error(error)
            json_result = jsonable_encoder({"result" : "Error division for zero"})

        return JSONResponse(content=json_result)

    #metodo com a operacao de multiplicar
    def multiplicar(self, arq1, arq2):
        try:
            result = {"result" : arq1 * arq2}
            json_result = jsonable_encoder(result)
        except:
            raise
        return JSONResponse(content=json_result)
    
    #metodo com a operacao de multiplicar
    def subtrair(self, arq1, arg2):
        try:
            result = {"result" : arq1 - arg2}
            json_result = jsonable_encoder(result)
        except:
            raise
        return JSONResponse(content=json_result)
