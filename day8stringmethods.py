#string methods 
  #1.capitalize()
  #2.upper()
  #3.lower()
  #4.strip()
  #5.slice()
  
quote1 = "----Dream is not something-that you see in sleep, Dream is something that does not let you sleep----"
print(quote1.strip("-"))
print(quote1.lstrip("-"))
print(quote1.rstrip("-"))

# task 2
message="     🐫🕑🕝🔑secret_code✌️"
code="SECRET_CODE✌️"
position=message.find("🔑")+1
output=message[position:].upper()
 
if(output==code):
    print("you are an hacker")
else:
    print("Try again")