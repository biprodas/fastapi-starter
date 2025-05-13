from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
)
from typing import Union, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Book(BaseModel):
    id: Optional[int] = Field(default=None, description="Id is not needed on create")
    title: str = Field(min_length=3, max_length=50, description="The title of the book")
    author: str = Field(min_length=1, description="The author of the book")
    description: str = Field(min_length=3, max_length=100, description="The description of the book")
    rating: float = Field(gt=0, lte=5.0, description="The rating of the book")
    published_date: datetime = Field(description="The published date of the book")
    price: float = Field(gt=0, description="The price of the book")
    is_offer: Union[bool, None] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                  "title": "The Great Gatsby", 
                  "author": "F. Scott Fitzgerald", 
                  "description": "A novel about the American Dream", 
                  "rating": 4.5, 
                  "price": 10.99, 
                  "published_date": "2021-01-01",
                  "is_offer": False
                },{
                  "title": "To Kill a Mockingbird", 
                  "author": "Harper Lee", 
                  "description": "A novel about the American Dream", 
                  "rating": 4.5, 
                  "price": 10.99, 
                  "published_date": "2021-01-01",
                  "is_offer": False
                },{
                  "title": "1984", 
                  "author": "George Orwell", 
                  "description": "A novel about the American Dream", 
                  "rating": 4.5, 
                  "price": 10.99, 
                  "published_date": "2021-01-01",
                  "is_offer": False
                }
            ]
        }
    }    

class BookUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=50, description="The title of the book")
    author: Optional[str] = Field(default=None, min_length=1, description="The author of the book")
    description: Optional[str] = Field(default=None, min_length=3, max_length=100, description="The description of the book")
    rating: Optional[int] = Field(default=None, gt=0, lt=6, description="The rating of the book")
    price: Optional[float] = Field(default=None, gt=0, description="The price of the book")
    is_offer: Optional[bool] = None
    published_date: Optional[datetime] = Field(default=None, description="The published date of the book")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                  "title": "The Great Gatsby", 
                  "author": "F. Scott Fitzgerald", 
                  "description": "A novel about the American Dream", 
                  "rating": 4.5,
                  "price": 10.99, 
                  "is_offer": False,
                  "published_date": "2021-01-01"
                }
            ]
        }
    }
    
    
route = APIRouter(prefix="/books", tags=["Book"])
    

@route.get("", status_code=status.HTTP_200_OK)
def read_all_books(q: Union[str, None] = None):
    return [
      {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A novel about the American Dream",
        "rating": 4.5,
        "price": 10.99,
        "is_offer": False,
        "published_date": "2021-01-01"
      },
      {
        "id": 2,
        "title": "To Kill a Mockingbird", 
        "author": "Harper Lee",
        "description": "A novel about the American Dream",
        "rating": 4.5,
        "price": 10.99,
        "is_offer": False,
        "published_date": "2021-01-01"
      },
      {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "description": "A novel about the American Dream",
        "rating": 4.5,
        "price": 10.99,
        "is_offer": False,
        "published_date": "2021-01-01"
      }
    ]


@route.get("/{book_id}", status_code=status.HTTP_200_OK)
def read_book(book_id: int):
    found = book_id != 9
    if not found:
        raise HTTPException(status_code=404, detail="Book not found")
    return {
        "id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A novel about the American Dream",
        "rating": 4.5,
        "price": 10.99,
        "is_offer": False,
        "published_date": "2021-01-01"
      }
  
  
@route.post("", status_code=status.HTTP_201_CREATED)
def create_book(book_request: Book):
    return book_request
  

@route.put("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_book(book_id: int, book: BookUpdate):
    found = book_id != 9
    if not found:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book_id, "book_name": book.title}
  

@route.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    return {"book_id": book_id, "msg": "Book deleted successfully"}
  

