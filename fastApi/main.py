from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def alldata():
    return {
        "message": "hello world"
    }
