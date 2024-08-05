from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "history"},
    {"title": "Title Three", "author": "Author Two", "category": "science"},
    {"title": "Title Four", "author": "Author Four", "category": "mathematics"},
    {"title": "Title Five", "author": "Author Five", "category": "science"},
    {"title": "Title Six", "author": "Author Six", "category": "science"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# path parameters
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# query parameters


@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{author}/")
async def read_books_by_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("category").casefold() == category.casefold()
            and book.get("author").casefold() == author.casefold()
        ):
            books_to_return.append(book)
    return books_to_return
