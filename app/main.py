from fastapi import FastAPI

#from models import Item

from typing import Optional
from pydantic import BaseModel
from app.models import Item


app = FastAPI()

@app.get("/")
def index():
    return {"Avaliação Tecnica":"Tiago Samapaio",
            "Status": "Em Andamento"}

@app.post("/calcula/")
async def calculet_item(item:Item):
        item_dict = item.dict()   
        if isinstance(item_dict,dict):
            if item_dict['acao'] == 'sum':
                item_dict.update({"result":item_dict['price'] + item_dict['juros']})
            elif item_dict['acao'] == 'sub':
                item_dict.update({"result":item_dict['price'] - item_dict['juros']})
            elif item_dict['acao'] == 'mul':
                item_dict.update({"result":item_dict['price'] * item_dict['juros']})
            elif item_dict['acao'] == 'div' and item_dict['juros'] != 0:
                item_dict.update({"result":item_dict['price'] / item_dict['juros']})
            else:
                item_dict.update({"result":"Operação não encontrada"})
            return item_dict
        else:    
            return  {"Error":"Only Json is Allowed"}
            

