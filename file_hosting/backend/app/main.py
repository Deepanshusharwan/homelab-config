from fastapi import FastAPI
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hello world"}

@app.get('/item/{item}')
async def read_items(item:int):
    'read items get'
    return {"item": item}


@app.get('/something/{model_name}')
async def get_mode(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name}
    if model_name.value == 'lenet':
        return {'model_name': model_name}
    return {model_name}


