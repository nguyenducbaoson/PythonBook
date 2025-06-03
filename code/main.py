from fastapi import FastAPI, APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from configurations import collection, users_collection
from database.schemas import all_data
from database.models import Book, Token, User, UserOut, UserCreate
from auth.auth_handler import authenticate_user, create_access_token, get_current_user, get_password_hash
from uuid import uuid4
from datetime import datetime, timedelta

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

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/user/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/user/me/items", response_model=User)
async def read_own_items(current_user: User = Depends(get_current_user)):
    return [{"item_id": 1, "owner": current_user.username}]

@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate):
    # hash password
    hashed_pw = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_pw
    del user_dict["password"]
    
    # kiểm tra trùng user
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")

    users_collection.insert_one(user_dict)
    return UserOut(**user_dict)

app.include_router(router)
