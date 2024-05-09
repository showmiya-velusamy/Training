# while loop
# no_of_stars = 5
# ✨
# pattern printing using while
no_of_stars = 5
i = 0
while i < no_of_stars:
    print("✨" * (i + 1))
    i += 1

#for loop
#no_of_stars = 5
# ✨
#pattern printing using for loop
no_of_stars=5
for i in range(no_of_stars):
  print('✨'*(i+1))
  i+=1

#double the array values by for loop  
player_status=[10,20,30]
for i in range(len(player_status)):
  player_status[i]*=2
print(player_status)

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
 
# Output
# [4, 8, 11, 15, 10, 4]
# Task 4.1 - for loop
lengths = []
for name in avengers:
    lengths.append(len(name))
print(lengths)
# Task 4.2 - List comprehension
lengths = [len(name) for name in avengers]
print(lengths)

large_count = []
for count in letters_count:
    if count > 10:
        large_count.append(count)
print(large_count)
 
# Select count from letters_count where count > 10
# Give me count for each count in letters_count where count > 10
large_count_1 = [count for count in letters_count if count > 10]
print(large_count_1)
 
 
avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
 
# Output
# [
#     "Black widow",
#     "Captain america",
# ]
 
new_array = []
for i in avengers:
    if len(i) > 10:
        new_array.append(i)
print(new_array)

#task 5.2 -list comprehension
new_array=[i for i in avengers if len(i)>10]
print(new_array)
 
 
