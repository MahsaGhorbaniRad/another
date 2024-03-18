#پوشه ای شامل تمام شهر های کشور در همان فایلی که شامل تمارین است ذخیره
# و از کتابخانه ی پانداس برای خواندن آن ها استفاره کرده ام  

from fastapi import FastAPI
import pandas as pd

df = pd.read_csv("cities.csv")

app = FastAPI()

@app.get("/home/{city}")

def cities(city):
    if city == df["province_id"]:
        return f"valid"
