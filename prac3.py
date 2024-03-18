from fastapi import FastAPI

app = FastAPI()

@app.get("/home/")

def birth_date(date):
    date = str(date)
    sum = 0
    for i in date:
        if i == "/":
            break
        sum += 1
    if sum != 4:
        return f".قسمت سال نادرست است"
    if date[5] == "1":
        if date[6] != "0" and date[6] != "1" and date[6] != "2":
            return f".قسمت ماه نادرست است"
    if date[5] == "0" and date[6] == "0":
            return f".قسمت ماه نادرست است"
    if int(date[8]) > 3:
        return f".قسمت روز نادرست است"
    if int(date[8]) == 3:
         if date[9] != "0" and date[9] != "1":
              return f".قسمت روز نادرست است"
    if date[8] == "0" and date[9] == "0":
            return f".قسمت روز نادرست است"
    else:
        return f".تاریخ تولد وارد شده درست است"

        