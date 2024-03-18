from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{name}")

def my_Func(name : str):
    sum = 0
    for i in name:
        sum += 1
        if ord(i) != 32:
            if not("آ" <= i <= "ی"):
                return f".نام فقط حاوی حروف فارسی و بدون علایم خاص باشد"
    if sum > 10:
        return f".نام حداکثر حاوی 10 کاراکتر باشد"
    else:
        return name