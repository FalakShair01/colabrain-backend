from fastapi import Depends, FastAPI
import models
from database import engine
from routers import organization, chatting, authentication

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(authentication.router)
app.include_router(organization.router)
app.include_router(chatting.router)



@app.get("/")
async def root():
    return {"message": "Welcome to Colabrain Applications!"}
