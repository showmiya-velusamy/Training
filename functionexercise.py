library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True
    },
    {
        "title": "Advance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False
    },
]

# Task 1
# Add Book Function: Write a function add_book(library, new_book)
def add_book(library,new_book):
    library.append(new_book)
    return library
new_book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}
add_book(library_list,new_book)
print(library_list)

# Task 2
# Search Books by Author Function: Write a function search_by_author(library, author_name)
def search_by_author(library_list, author_name):
    found_books = []
    for book in library_list:
        if book.get("author") == author_name:
            found_books.append(book)
    return found_books
print(search_by_author(library_list,"Mark Lutz"))

# Task 3
# Check Out Book Function: Write a function check_out_book(library, title) that marks 
# a book as not available if it exists and is available in the library.
def book_checking(library, title):
    for book in library:
        if book.get("title") == title and  book["available"] == True:
            book["available"] = False
            return(f"The book '{title}' is available.")
        else:
            return(f"The book '{title}' is not available.")
    print(f"The book '{title}' was not found in the library.")
print(book_checking(library_list, "Advance Python"))

def own_max(*nums):
     l = nums[0]
     for num in nums:
          if num > l:
               l = num
     return l
print(own_max(5, 6, 10))
print(own_max(5, 6, 10, 7, 80, 60))