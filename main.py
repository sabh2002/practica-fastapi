from fastapi import FastAPI
from routes.usuarios import principal

app = FastAPI()

app.include_router(principal)


