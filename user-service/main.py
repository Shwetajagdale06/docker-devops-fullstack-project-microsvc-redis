from fastapi import FastAPI
import psycopg2
import redis

r = redis.Redis(host="redis", port=6379)

app = FastAPI()


@app.get("/cache")
def cache_example():
    r.set("key", "value")
    return {"cached": r.get("key").decode()}


@app.get("/users")
def get_users():
    return {"message": "List of users"}

