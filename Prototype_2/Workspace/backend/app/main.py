from fastapi import FastAPI
from . import app

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}