from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/home/{string}")

def is_valid_phone(string):
    phone_regex = "^0[0-9]{2}[0-9]{8}$"
    if re.search(phone_regex , string):
        return f".شماره تلفن ثابت وارد شده درست است"
    return f".شماره تلفن ثابت وارد شده نادرست است"