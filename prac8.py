from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{code_posti}")

def code_posti(code_posti):
    code_posti = str(code_posti)
    sum = 0
    for i in code_posti:
        sum += 1
    if sum == 10 and (48 <= ord(i) <= 57):
        return f".کد پستی وارد شده درست است"
    else:
        return f".کد پستی وارد شده نادرست است"