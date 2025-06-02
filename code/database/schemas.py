def individual_data(book):
    return {
        "id": str(book.get("id", "")),  # ← dùng id bạn tự sinh
        "title": book.get("title", ""),
        "author": book.get("author", ""),
        "description": book.get("description", ""),
        "year": book.get("year", ""),
    }

def all_data(books):
    return [individual_data(book) for book in books]
