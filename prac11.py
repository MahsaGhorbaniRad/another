from fastapi import FastAPI

app = FastAPI()


@app.get("/home/{college}")

def college(college):
    C = ["فنی و مهندسی" , "علوم پایه" , "علوم انسانی" , "دامپزشکی" , "اقتصاد" , "کشاورزی" , "منابع طبیعی"]
    for i in C:
        if college == i:
            return f".دانشکده وارد شده معتبر است" 
    return f".دانشکده وارد شده نامعتبر است"