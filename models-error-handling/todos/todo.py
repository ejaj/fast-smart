from fastapi import APIRouter, Path, HTTPException, status
from .model import TodoItems, TodoItem, Todo

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    """

    Args:
        todo:

    Returns:

    """
    todo_list.append(todo)
    return {"message": "Todo added successfully."}


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    """

    Args:
        todo_id:

    Returns:

    """
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo item not found."
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    """

    Args:
        todo_data:
        todo_id:

    Returns:

    """
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    """

    Args:
        todo_id:

    Returns:

    """
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id: todo_list.pop(index)
        return {"message": "Todo deleted successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist",
    )
