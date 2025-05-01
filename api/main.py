from fastapi import FastAPI
from api.routers import english_word

app = FastAPI()

app.include_router(english_word.router)
