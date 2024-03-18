from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/home/{mobile}")

def is_valid_mobile(mobile):
    mobile_regex = "^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$"
    if re.search(mobile_regex , mobile):
        return f".شماره تلفن همراه وارد شده درست است"
    return f".شماره همراه وارد شده نادرست است"        