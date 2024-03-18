from fastapi import FastAPI
from pydantic import BaseModel

class adress(BaseModel):
    adress : str

app = FastAPI()

@app.post("/home/")

def Adress(adress:adress):
    adress = str(adress)
    sum = 0
    for i in adress:
        sum += 1
    if sum <= 100:
        return f".آدرس وارد شده درست است"
    else:
        return f".آدرس وارد شده نادرست است"