from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from transformers import pipeline

app = FastAPI()

# Load the language model for text generation
text_generation_model = pipeline('text-generation', model='gpt-3.5-turbo')

class GenreRequest(BaseModel):
    genre: str

class BookSelectionRequest(BaseModel):
    top_10: List[str]
    user_preference: str

def fetch_top_100_books(genre):
    # Mock implementation: Replace with actual logic to fetch books from a database or API
    return [f"Book {i} - {genre}" for i in range(1, 101)]

def filter_top_10_books(genre):
    # Mock implementation: Filter top 10 books from top 100
    top_100_books = fetch_top_100_books(genre)
    return top_100_books[:10]

def find_top_book(top_10, user_preference):
    # Mock implementation: Select a book based on user preference
    return top_10[0]  # Simplified selection logic

@app.post("/get_top_100_books")
async def get_top_100_books(request: GenreRequest):
    top_100_books = fetch_top_100_books(request.genre)
    return {"top_100_books": top_100_books}

@app.post("/get_top_10_books")
async def get_top_10_books(request: GenreRequest):
    top_10_books = filter_top_10_books(request.genre)
    return {"top_10_books": top_10_books}

@app.post("/get_top_book")
async def get_top_book(request: BookSelectionRequest):
    top_book = find_top_book(request.top_10, request.user_preference)
    return {"top_book": top_book}

@app.get("/thank_you")
async def thank_you():
    return {"message": "Thank you for using our service!"}

@app.post("/generate_text")
async def generate_text(prompt: str):
    try:
        # Generate text based on the prompt using the text generation model
        generated_text = text_generation_model(prompt, max_length=100, num_return_sequences=1)

        return {"generated_text": generated_text[0]['generated_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
