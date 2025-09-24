from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books/{book_id}")
async def available_book(book_id: int):
    return {"book_id": book_id, "title": "Sample Book", "author": "Author Name"}