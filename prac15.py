from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class student(BaseModel):
    student_number : str
class name(BaseModel): 
    name : str
class date(BaseModel):
    date : str
class serial(BaseModel):
    serial : str
class shahr(BaseModel):
    shahr : str
class adress(BaseModel):
    adress: str
class code_posti(BaseModel):
    code_posti : str
class mobile(BaseModel):
    mobile: str
class phone(BaseModel):
    phone: str
class college(BaseModel):
    college: str
class field(BaseModel):
    field: str
class marital_status(BaseModel):
    marital_status: str
class code(BaseModel):
    code: str

@app.post("/home")

def read(data:dict):
    false = []
    student_number = data.get("student_number" , str)
    if len(student_number) != 11:
        false.append("شماره دانشجویی باید 11 رقم باشد. تعداد ارقام وارد شده نادرست است")
    if int(student_number[0:3]) < 400 or int(student_number[0:3]) > 402:
        false.append(".قسمت سال نادرست است")
    if int(student_number[3:9]) != 114150:
        false.append(".قسمت ثابت نادرست است")
    if int(student_number[9]) == 0:
        if int(student_number[10]) == 0:
            false.append(".قسمت اندیس نادرست است")
    # else:
    #     return f".شماره دانشجویی وارد شده درست است"
    

    
    name = data.get("name" , str)
    sum = 0
    for i in name:
        sum += 1
        if ord(i) != 32:
            if not("آ" <= i <= "ی"):
                false.append(".نام فقط حاوی حروف فارسی و بدون علایم خاص باشد")
    if sum > 10:
        false.append(".نام حداکثر حاوی 10 کاراکتر باشد")
    # else:
    #     return name
    

    date = data.get("data" , str)
    sum = 0
    for i in date:
        if i == "/":
            break
        sum += 1
    if sum != 4:
        false.append(".قسمت سال نادرست است")
    if date[5] == "1":
        if date[6] != "0" and date[6] != "1" and date[6] != "2":
            false.append(".قسمت ماه نادرست است")
    if date[5] == "0" and date[6] == "0":
            false.append(".قسمت ماه نادرست است")
    if int(date[8]) > 3:
        false.append(".قسمت روز نادرست است")
    if int(date[8]) == 3:
         if date[9] != "0" and date[9] != "1":
              false.append(".قسمت روز نادرست است")
    if date[8] == "0" and date[9] == "0":
            false.append(".قسمت روز نادرست است")
    # else:
    #     return f".تاریخ تولد وارد شده درست است"
    
    

    serial = data.get("serial" , str)
    num = 0
    for i in serial:
        if i == "/":
            break
        if not(48 <= ord(i) <= 57):
            continue
        num += 1
    if num != 2:
        false.append(".دو رقم ابتدایی شماره شناسنامه نادرست وارد شده است")
    sum = 0
    if num == 2:
        for i in serial[4:]:
            sum += 1
        if sum != 6:
            false.append(".شش رقم پایانی نادرست وراد شده است" )
        # else:
        #     return f".سریال شناسنامه وارد شده درست است"
        


    shahr = data.get("shahr" , str)
    a = ["خرم آباد" , "تهران" , "مشهد" , "اصفهان" , "شیراز" , "تبریز" , "ارومیه" , "ایلام" , "یزد" , "کرمان" , "بیرجند" , "زاهدان" , "بندرعباس" , "بوشهر" , "شهرکرد" , "اراک", "گرگان" , "بجنورد" , "ساری" , "سمنان" , "قم" , "قزوین" , "رشت" , "زنجان" , "سنندج" , "اردبیل" , "کرمانشاه" , "اهواز" , "همدان" , "یاسوج" ,]
    for i in a:
        if shahr != i:
            false.append(".شهر وارد شده مرکز استان نیست")

        

    adress = data.get("adress" , str)
    sum = 0
    for i in adress:
        sum += 1
    if not(sum <= 100):
        false.append(".آدرس وارد شده نادرست است")
    

    code_posti = data.get("code_posti" , str)
    sum = 0
    for i in code_posti:
        sum += 1
    if not(sum == 10 and (48 <= ord(i) <= 57)):
        false.append(".کد پستی وارد شده نادرست است")


    
    mobile = data.get("mobile" , str)
    mobile_regex = "^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$"
    if re.search(mobile_regex , mobile):
        return f".شماره تلفن همراه وارد شده درست است"
    false.append(".شماره همراه وارد شده نادرست است"  )      



    phone = data.get("phone" , str)
    phone_regex = "^0[0-9]{2}[0-9]{8}$"
    if re.search(phone_regex , phone):
        return f".شماره تلفن ثابت وارد شده درست است"
    false.append(".شماره تلفن ثابت وارد شده نادرست است")



    college = data.get("college" , str)
    C = ["فنی و مهندسی" , "علوم پایه" , "علوم انسانی" , "دامپزشکی" , "اقتصاد" , "کشاورزی" , "منابع طبیعی"]
    for i in C:
        if college != i:
            false.append(".دانشکده وارد شده نامعتبر است")

        

    field = data.get("field" , str)
    F = ["مهندسی کامپیوتر" , "مهندسی صنایع" , "مهندسی پزشکی" , "مهندسی عمران" , "مهندسی مکانیک" , "مهندسی پلیمر" , "مهندسی نفت" , "مهندسی معدن"]
    for i in F:
        if field != i:
            false.append(".رشته تحصیلی وارد شده نامعتبر است")

        

    marital_status = data.get("marital_status" , str)
    if marital_status:
        return f"valid"
    
    

    code = data.get("code" , str)
    code_regex = "^([0-9]){10}"
    if re.search(code_regex , code):
        return f".کد ملی وارد شده معتبر است"
    false.append(".کد ملی وارد شده نامعتبر است")

    if false:
        return false
    else:
        return f".مورد نامعتبری وجود ندارد"