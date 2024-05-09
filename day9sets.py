colors = ["red", "blue", "red", "blue", "green"]
print(set(colors))

# Output
# [6.4, 1.414, 11.66, 13.45]
# Task 1 : Finding the distance between given coordinates and origin
coordinates = [(5,4) , (1,1), (6,10), (9,10)]
distance = []
for (x,y) in coordinates:
    distance.append(((x**2) + (y**2))**0.5)
print(distance)

#task-2- for loop and unpacked
d=[]
for coordinate in coordinates:
    x,y =coordinate
    d.append((x**2 + y**2)**0.5)
print(d)

#task 3-list comprehension
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distance=[round((x**2 + y**2)**0.5) for x,y in coordinates]
print(distance)