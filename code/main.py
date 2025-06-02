from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_data
from database.models import Book

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
        resp = collection.insert_one(dict(new_book))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred {e}")

app.include_router(router)
