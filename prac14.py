from fastapi import FastAPI
import re

app = FastAPI()

#سلام استاد من نمی دونستم منظورتون از اینکه کد ملی مطابق استاندارد ایران باشه چیه
# درواقع مطمین نبودم منظورتون بررسی معتبر بودن کد ملی از طریق فرمول هست یا صرفا بررسی 
# ده رقمی بودن کد ملی هست. بنابراین هر دو رو نوشتم


@app.get("/inside/{code}")

def code_meli(code):
    code_regex = "^([0-9]){10}"
    if re.search(code_regex , code):
        return f".کد ملی وارد شده معتبر است"
    return f".کد ملی وارد شده نامعتبر است"



@app.get("/home/{code}")

def code_meli(code):
    sum = 0
    code = str(code)
    if len(code) == 10:
        for i in range(10 , 1 , -1):
            sum += code[10 - i] * i
        if (sum % 11) >= 2:
            if (11 - (sum % 11)) == code[9]:
                return f".کد ملی وارد شده معتبر است"
        elif (sum % 11) < 2:
            if (sum % 11) == code[9]:
                return f".کد ملی وارد شده معتبر است"
        else:
            return f".کد ملی وارد شده نامعتبر است"
    else:
        return f".ملی وارد شده باید حاوی 10 رقم باشد"
    
