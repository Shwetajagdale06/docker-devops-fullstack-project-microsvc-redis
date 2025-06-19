from fastapi import FastAPI

app = FastAPI()

@app.get("/notes")
def get_notes():
    return {"message": "List of notes"}
