from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/home/{student_number}")

def read(student_number):
    student_number = str(student_number)
    if len(student_number) != 11:
        return f"شماره دانشجویی باید 11 رقم باشد. تعداد ارقام وارد شده نادرست است"
    if int(student_number[0:3]) < 400 or int(student_number[0:3]) > 402:
        return f".قسمت سال نادرست است"
    if int(student_number[3:9]) != 114150:
        return f".قسمت ثابت نادرست است"
    if int(student_number[9]) == 0:
        if int(student_number[10]) == 0:
            return f".قسمت اندیس نادرست است"
    else:
        return f".شماره دانشجویی وارد شده درست است"
    

@app.get("/page/")

def func(student_number):
    student_number = str(student_number)
    if len(student_number) != 11:
        return f"شماره دانشجویی باید 11 رقم باشد. تعداد ارقام وارد شده نادرست است"
    if int(student_number[0:3]) < 400 or int(student_number[0:3]) > 402:
        return f".قسمت سال نادرست است"
    if int(student_number[3:9]) != 114150:
        return f".قسمت ثابت نادرست است"
    if int(student_number[9]) == 0:
        if int(student_number[10]) == 0:
            return f".قسمت اندیس نادرست است"
    else:
        return f".شماره دانشجویی وارد شده درست است"
    

class student_number(BaseModel):
    student_number : int

@app.post("/out/")

def req(std:student_number):
    std = str(std)
    if len(std) != 26:
        return f"شماره دانشجویی باید 11 رقم باشد. تعداد ارقام وارد شده نادرست است"
    if int(std[15:18]) < 400 or int(std[15:18]) > 402:
        return f".قسمت سال نادرست است"
    if int(std[18:24]) != 114150:
        return f".قسمت ثابت نادرست است"
    if int(std[24]) == 0:
        if int(std[25]) == 0:
            return f".قسمت اندیس نادرست است"
    else:
        return f".شماره دانشجویی وارد شده درست است"