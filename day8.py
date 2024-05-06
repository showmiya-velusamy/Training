print("Hello World")
#declare and assign
name="showmiya"
print(name)
print(type(name))
age=21
print(age)
print(type(age))
print("Hello my name is "+name)
name =input("Enter your name:")
print("Hello my name is "+name)
print('nice'*2)
#task 1
#fahreneit to celcius
# The equivalent of 98.6°F is 37°C
fahrenheit = float(input("Enter your body temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("The equivalent of " + str(fahrenheit) + "°F is " + str(celsius) + "°C")
#task 2
#Find the age of the person given the birth year 2000
birth_year=int(input("enter your birth year: "))
age=2024 - birth_year
print(f"The present age is {age} years")
#f-strings
fahrenheit = float(input("Enter your body temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"The equivalent of {fahrenheit}°F is {celsius}°C")
#value inside curly braces is interpolation
#task 3
#print the area of circle-f string
radius=float(input("The radius of circle is: "))
Area=3.14*int(radius)**2
print(f"The area of circle is {Area} cm^2")
#task 4 
#build a loader
#input=70
#output=[======= ]70%
percentage=int(input("enter the input :"))
equals = int(percentage / 10)
loader = '[' + '=' * equals + ' ' * (10 - equals) + ']' + f"{percentage}%"
print(loader)