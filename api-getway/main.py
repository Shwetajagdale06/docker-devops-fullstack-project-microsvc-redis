from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/users")
async def forward_to_user():
    async with httpx.AsyncClient() as client:
        r = await client.get("http://user-service:8001/users")
    return r.json()

@app.get("/notes")
async def forward_to_note():
    async with httpx.AsyncClient() as client:
        r = await client.get("http://note-service:8002/notes")
    return r.json()
