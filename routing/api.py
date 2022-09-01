from fastapi import FastAPI

from todos.todos import todo_router

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router)
