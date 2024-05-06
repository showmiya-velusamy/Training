#slicing method

quote = "Dream is something"
# print(quote[<start>: <end>: <skip>])
print(quote[1:3])  # re
print(quote[-1])  # m
 
print(quote[-4:-1])  # rea
 
 
print(quote[1:10:2])  # ra ss
print(quote[::-1])  # gnihtemos si maerD #can be used in palindrome also
print(quote[-1:-4:-1]) # gni

#palindrome
name="malayalam"
print(name[::1])

#Task2
message = "    🚨🔍📱🔑****secret_code✌️(((("
code = "SECRET_CODE✌️"
index=message.find('🔑')
message = message[index+1:]
message = message.strip('*') 
message=message.strip('(')
if (message.upper() == code):
  print("You are an hacker")
else:
  print("Try again")
  
#another way
message1 = "    🚨🔍📱🔑*******secret_code✌️((("
secret_message = message1.replace("*", "").replace("(", "")[message1.find('🔑')+1:]
print(secret_message.upper())