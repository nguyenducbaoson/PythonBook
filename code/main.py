from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_data
from database.models import Book
from uuid import uuid4

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_books():
    try:
        data = list(collection.find())
        return all_data(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {e}")

@router.post("/")
async def create_book(new_book: Book):
    try:
        book_dict = new_book.dict()
        book_dict["id"] = str(uuid4())

        resp = collection.insert_one(book_dict)
        return {"status_code": 200, "id": book_dict["id"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred {e}")

app.include_router(router)
