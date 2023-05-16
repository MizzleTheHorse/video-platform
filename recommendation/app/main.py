from fastapi import FastAPI
from .ORM_CRUD_recommendation import DatabaseInterface


app = FastAPI()

db = DatabaseInterface()


@app.get("/random_recommend")
def recommend():
    return {"recommendations": "list of videos here"}


@app.get("/recommend/{user_id}")
def recommend_user(user_id):
    result = db.get_latest_user_actions(user_id=user_id)
    if not result: 
        return {"recommendations": 'No recommendations available.'}
    return {"recommendations": str(result)}


@app.get("/recommend/")
def recommend_user_with_action(user_id: int, action: str):
    result = db.get_latest_user_actions_with_param(user_id=user_id, action=action)
    if not result: 
        return {"recommendations": 'No recommendations available.'}
    return {"recommendations": str(result)}



