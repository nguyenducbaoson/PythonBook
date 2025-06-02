def individual_data(book):
    return {
        "id": str(book.id),
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "year": book.year,
    }

def all_data(books):
    return [individual_data(book) for book in books]