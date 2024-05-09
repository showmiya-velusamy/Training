# Why?: Motivation of function
 
 
a = 8
b = 10
 
print("The sum is: ", a + b)
 
 
a1 = 60
b1 = 70
 
print("The sum is: ", a1 + b1)
 
a2 = 600
b2 = 70
 
print("The sum is: ", a2 + b2)
 
 
# Function
# 1. Declaration / Definition
# 2. Function name
# 3. Parameters - 2
# 4. Function body
def add(a, b):
    return round(a + b, 2)
 
 
# Function call
print("The sum is: ", add(8, 10))
print("The sum is: ", add(60, 70))
print("The sum is: ", add(600, 70))  # arguments
print("The sum is: ", add(60.748494, 70.89898))
print("The sum is: ", add(160.748494, 170.89898))
 
 
# Default values
def driving_test(name, age, car="Dezire"):
    if age >= 18:
        return f"{name} eligible for driving. You will be tested in {car}"
    else:
        return "Try again after few years 👶🍼"
 
 
print(driving_test("Sai Subash", 20, "Creata"))
print(driving_test("Sai Ganesh", 20))
 
 
# Types of argument
# 1. Position argument
# 2. Keyword argument
 
# Position argument
# print(driving_test(20, "Poojitha"))
 
# Keyword argument
print(driving_test(age=20, name="Poojitha"))
print(driving_test("Abishek", car="Honda city", age=20))

movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]
# Function
# Task 1
# get_movies_avg_rating
# Import package - Inbuilt
# from package_name import function_name
from pprint import pprint
def average_ratings(movies):
    for movie in movies:
        movie['average_rating'] = sum(movie['ratings']) / len(movie['ratings'])
    return movies
print(average_ratings(movies))
# Task 2 - break it into 2 functions
from pprint import pprint
def avg_rating(movie):
    movie['avg_rating'] = sum(movie['ratings']) / len(['ratings'])
    return avg_rating
def append_avg_ratings(movies):
    for movie in movies:
        average_rating = avg_rating(movie)
        movie["average_rating"] = average_rating
    return movies
print(movies)
