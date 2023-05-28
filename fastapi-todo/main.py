from fastapi import FastAPI
import uvicorn

from views.todo_items import router as todo_items_router

app = FastAPI()
app.include_router(todo_items_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
