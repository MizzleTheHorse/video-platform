from fastapi import FastAPI

app = FastAPI()


@app.get("/recommend_no_login")
def hello_world():
    return {"recommendations": "list of videos here"}
