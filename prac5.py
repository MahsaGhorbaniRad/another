from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{shahr}")

def Ostan(shahr):
    a = ["خرم آباد" , "تهران" , "مشهد" , "اصفهان" , "شیراز" , "تبریز" , "ارومیه" , "ایلام" , "یزد" , "کرمان" , "بیرجند" , "زاهدان" , "بندرعباس" , "بوشهر" , "شهرکرد" , "اراک", "گرگان" , "بجنورد" , "ساری" , "سمنان" , "قم" , "قزوین" , "رشت" , "زنجان" , "سنندج" , "اردبیل" , "کرمانشاه" , "اهواز" , "همدان" , "یاسوج" ,]
    for i in a:
        if shahr == i:
            return f". شهر وارد شده مرکز استان است"
    return f".شهر وارد شده مرکز استان نیست"