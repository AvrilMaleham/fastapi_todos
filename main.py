from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, user

app = FastAPI()

# Generate .db file, only runs once to create
models.Base.metadata.create_all(bind=engine)

@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)

        