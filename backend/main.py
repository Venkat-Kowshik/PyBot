from fastapi import FastAPI
from  fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRIVATE_KEY = "3208c8b3-8506-4aa4-a55c-6aed2ab61b68"

class User(BaseModel):
    username:str
@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data = {
            "username": user.username,
            "secret":user.username,
            "first_name": user.username,
        },
        headers={"Project-ID":PRIVATE_KEY}                    
    )
    return response.json()    