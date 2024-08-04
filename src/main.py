import uvicorn
from fastapi import FastAPI
from src.routers import habit, user

app = FastAPI()


app.include_router(habit.habit_routers)
app.include_router(user.user_routers)
if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True, port=8000)
