#hit_books=[]
#for book in books:
#  if(book['rating']>=4.7):
#    print(hit_books.append(book['title']))
#print(hit_books)

#hit_books=[book['title'] for book in books if book['rating']>=4.7]
#print(hit_books)
 
person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    # "stats": {"goals": 300, "assists": 500},
    "sport": "football",
    # "height": 168,
}
print(person['address']['country'])
# print(person["stats"]["goals"]) # KeyError: 'stats'
# print(person.get("stats").get("goals")) # 'NoneType' object has no attribute 'get'
 # Default value - person.get(key, default value)
print(person.get("height", 174))
print(person.get("stats", {}).get("goals"))  # None
print(person.get("stats", {"goals": 0}).get("goals"))  # None

employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
# Task: After 1 experience
for employee in employees:
    employee["experience"]=employee.get("experience",0)+1
print(employees)
# Output
#[
#   {"name": "Sneha", "experience": 3},
#   {"name": "Manju",  "experience": 1},
#   {"name": "Sai Subash", "experience": 5},
#    {"name": "Manasa", "experience": 1},
#]

# Task 2
#  Senior 5 or more, Mid-Level 3 to 5, Junior < 3


# Output
[
    {"name": "Sneha", "experience": 3, "status": "Mid-Level"},
    {"name": "Manju", "experience": 1, "status": "Junior"},
    {"name": "Sai Subash", "experience": 5, "status": "Senior"},
    {"name": "Manasa", "experience": 1, "status": "Junior"},
]
 
# Unpacking -> ** Dict
movie = {"name": "John wick", "year": 2014}
 
# Copy
mv1 = {**movie, "actor": "Keanu Reeves"}
mv2 = {**movie, "actor": "Keanu Reeves", "year": 2015}
mv3 = {"actor": "Keanu Reeves", "year": 2015, **movie}
print(mv1)
print(mv2)
print(mv3)
print(movie)