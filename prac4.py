from fastapi import FastAPI

app = FastAPI()

@app.get("/home/")

def serial(serial):
    serial = str(serial)
    num = 0
    for i in serial:
        if i == "/":
            break
        if not(48 <= ord(i) <= 57):
            continue
        num += 1
    if num != 2:
        return f".دو رقم ابتدایی شماره شناسنامه نادرست وارد شده است"
    sum = 0
    if num == 2:
        for i in serial[4:]:
            sum += 1
        if sum != 6:
            return f".شش رقم پایانی نادرست وراد شده است" 
        else:
            return f".سریال شناسنامه وارد شده درست است"
    
    