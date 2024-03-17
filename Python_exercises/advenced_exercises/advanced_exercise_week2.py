import itertools

books = [
    {
    "title": "Title1",
    "author": "Author1",
    "year": 2020,
    "rating": 4.5,
    "genre": "Novel"
    },
    {
    "title": "Title2",
    "author": "Author2",
    "year": 2024,
    "rating": 4.8,
    "genre": "Science"
    },
    {
    "title": "Title3",
    "author": "Author3",
    "year": 2023,
    "rating": 4,
    "genre": "Science Fiction"
    },
    {
    "title": "Title4",
    "author": "Author1",
    "year": 2022,
    "rating": 3.5,
    "genre": "Fiction"
    }
]

# filter_by_author() function:
def filter_by_genre(books, genre):
    for book in books:
        if book["genre"] == genre:
            yield book

# Test code:
for book in filter_by_genre(books, "Science"):
    print(book)

# Output:
    # {'title': 'Title2', 'author': 'Author2', 'year': 2024, 'rating': 4.8, 'genre': 'Science'}

# top_rated_books() function: 
def top_rated_books(books, min_rating):
    for book in books:
        if book["rating"] >= min_rating:
            yield book

# Test code:
for book in top_rated_books(books, 4.5):
    print(book)

# Output:
    # {'title': 'Title1', 'author': 'Author1', 'year': 2020, 'rating': 4.5, 'genre': 'Novel'}
    # {'title': 'Title2', 'author': 'Author2', 'year': 2024, 'rating': 4.8, 'genre': 'Science'}

# sort_books() function:
def sort_books(books, key):
    if key == "title":
        sorted_books = sorted(books, key=lambda x: x["title"])
    elif key == "author":
        sorted_books = sorted(books, key=lambda x: x["author"])
    elif key == "year":
        sorted_books = sorted(books, key=lambda x: x["year"])
    elif key == "rating":
        sorted_books = sorted(books, key=lambda x: x["rating"])
    else:
        raise ValueError("Invalid sorting key")

    for book in sorted_books:
        yield book

# Test code:
for book in sort_books(books, "rating"):
    print(book)

# Output:
    # {'title': 'Title4', 'author': 'Author1', 'year': 2022, 'rating': 3.5, 'genre': 'Fiction'}
    # {'title': 'Title3', 'author': 'Author3', 'year': 2023, 'rating': 4, 'genre': 'Science Fiction'}
    # {'title': 'Title1', 'author': 'Author1', 'year': 2020, 'rating': 4.5, 'genre': 'Novel'}
    # {'title': 'Title2', 'author': 'Author2', 'year': 2024, 'rating': 4.8, 'genre': 'Science'}

# count_authors() function:
def count_authors(books):
    author_count = {}
    for book in books:
        author = book["author"]
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    return author_count

# Test code:
print(count_authors(books))

# Output:
    # {'Author1': 2, 'Author2': 1, 'Author3': 1}

# limit_results() function:
def limit_results(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            return itertools.islice(results, limit)
        return wrapper
    return decorator

# Test code:
@limit_results(2)
def top_rated_books(books, min_rating):
    for book in books:
        if book["rating"] >= min_rating:
            yield book

for book in top_rated_books(books, 3):
    print(book)

# Output:
    # {'title': 'Title1', 'author': 'Author1', 'year': 2020, 'rating': 4.5, 'genre': 'Novel'}
    # {'title': 'Title2', 'author': 'Author2', 'year': 2024, 'rating': 4.8, 'genre': 'Science'}
    