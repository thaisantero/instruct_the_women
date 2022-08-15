from typing import Union, Optional

from fastapi import FastAPI, Header

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    quantidade: Union[int, None] = 1
    valor: float


app = FastAPI()

banco_de_dados = []

# @app.post("/")
# def read_root(user_agent: Optional[str] = Header (None)):
#     return {"user_agent": user_agent}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[int, None] = None):
#     return {"item_id": item_quantidade, "q": q}

@app.post("/item")
def add_item(item: Item):
    banco_de_dados.append(item)
    return item

@app.get("/item/valor_total")
def get_valor_total(): 
	valor_total = 0.0
    # quantidade_total = 0
	for item in banco_de_dados:
		valor_total+=item.valor*item.quantidade
        # quantidade_total += item.quantidade
	return valor_total

@app.get("/item/quantidade_total")
def get_quantidade_total(): 
	quantidade_total = 0
	for item in banco_de_dados:
		quantidade_total+=item.quantidade
	return quantidade_total