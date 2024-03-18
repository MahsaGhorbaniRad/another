from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{marital_status}")

def marital_status(marital_status):
    if marital_status:
        return f"valid"
    