from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    env_name = os.getenv("ENV_NAME", "local")
    return {"message": f"Running in {env_name}"}
