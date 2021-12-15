from fastapi import APIRouter, Response, status
from sqlalchemy.sql.expression import select
from config.db import conn
from models.tweet import tweets
from schemas.tweet import Tweet
from cryptography.fernet import Fernet
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

tweet = APIRouter()

@tweet.get("/tweets")
def get_tweets():
    return conn.execute(tweets.select()).fetchall()

@tweet.post("/tweets", response_model=Tweet)
def post_tweet(tweet: Tweet):
    new_tweet = {"content": tweet.content}
    r = conn.execute(tweets.insert().values(new_tweet))
    return conn.execute(tweets.select().where(tweets.c.id == r.lastrowid)).first()

@tweet.delete("/tweets/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tweet(id:str):
    conn.execute(tweets.delete().where(tweets.c.id == id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)