from fastapi import FastAPI
from routers.user import user
from routers.tweet import tweet

app = FastAPI()

app.include_router(user)
app.include_router(tweet)