from fastapi import FastAPI

app = FastAPI()

@app.get("/home/")

def field(field):
    F = ["مهندسی کامپیوتر" , "مهندسی صنایع" , "مهندسی پزشکی" , "مهندسی عمران" , "مهندسی مکانیک" , "مهندسی پلیمر" , "مهندسی نفت" , "مهندسی معدن"]
    for i in F:
        if field == i:
            return f".رشته تحصیلی وارد شده معتبر است"
    return f".رشته تحصیلی وارد شده نامعتبر است"