hit_books=[]
for book in books:
  if(book['rating']>=4.7):
    print(hit_books.append(book['title']))
print(hit_books)

hit_books=[book['title'] for book in books if book['rating']>=4.7]
print(hit_books)

