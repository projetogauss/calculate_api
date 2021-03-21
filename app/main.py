from fastapi import FastAPI

#from models import Item

from typing import Optional
from pydantic import BaseModel
from app.models import Item


app = FastAPI()

@app.get("/")
def index():
    return {"Teste Capgemini":"Tiago Samapaio",
                                "Status": "Finalizado"}

@app.post("/calcula/")
async def calculet_item(item:Item):
        """Converte o obj em um dict"""
        item_dict = item.dict()
        """Check o tipo"""
        if isinstance(item_dict,dict):
            """Condicionais checam a acao"""
            if item_dict['acao'] == 'sum':
                item_dict = item.somar(item_dict['price'], item_dict['juros'])
            elif item_dict['acao'] == 'sub':
                item_dict = item.subtrair(item_dict['price'], item_dict['juros'])
            elif item_dict['acao'] == 'mul':
                item_dict = item.multiplicar(item_dict['price'], item_dict['juros'])
            elif item_dict['acao'] == 'div':
                item_dict = item.dividir(item_dict['price'], item_dict['juros'])
            else:
                item_dict.update({"result":"Not Found"})
            return item_dict
        else:    
            return  {"Error":"Only Json is Allowed"}
            

