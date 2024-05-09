# Idea
# Object Oriented Programming
# Modeling our problem as real-world objects
 
# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors
 
 
#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2
 
 
# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4
 
 
#  Car -> blueprint | Class blueprint object
 
 
class Car:
    def __init__(
        self, name, engine, wheels, doors
    ):  # creating object calls init (constructor)
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
 
 
ferrari = Car("Ferrari", "v8", 4, 2)  # object
alto = Car("Alto", "v4", 4, 4)  # object
 
print(ferrari.name, ferrari.wheels)

#task 1
class bank_account:
  def __init__(self,acc_no,name,balance=0):
     self.acc_no=self
     self.name=name
     self.balance=balance

acc1=bank_account(64834842,"sri",10000)
acc2=bank_account(28774341,"nithi",500)
acc3=bank_account(9763988,"kavya")
print(acc1.name)

#task 2
class bank_account:
  def __init__(self,acc_no,name,balance=0):
     self.acc_no=acc_no
     self.name=name
     self.balance=balance
  def display_balance(self):
    return(f"The balance of {self.name} is ₹{self.balance}")
acc1=bank_account(64834842,"sri",10_000)
acc2=bank_account(28774341,"nithi",500)
acc3=bank_account(9763988,"kavya")
print(acc1.display_balance())

#task 3
class bank_account:
  def __init__(self,acc_no,name,balance=0):
     self.acc_no=acc_no
     self.name=name
     self.balance=balance
  def display_balance(self):
    return(f"The balance of {self.name} is ₹{self.balance}")
  def withdraw(self,amount):
    if amount>self.balance:
      print("Insufficient balance")
    else:
      self.balance-=amount
      print(f"Withdrawal of ₹{amount} is successful")
    return(f"The amount withdrawn is ₹{amount} and the balance is ₹{self.balance}")

acc1=bank_account(64834842,"sri",10_000)
acc2=bank_account(28774341,"nithi",500)
acc3=bank_account(9763988,"kavya")
print(acc1.display_balance())
print(acc2.withdraw(500))

#task 4
def deposit(self,amount):
    self.balance+=amount
    print(f"Deposit of ₹{amount} is successful")
    return(f"The amount deposited is ₹{amount} and the balance is ₹{self.balance}")

def interest(self,rate,time):
    self.balance+=self.balance*rate*time
    print(f"The interest of ₹{self.balance*rate*time} is added to the balance")
    return(f"The interest is ₹{self.balance*rate*time} and the balance is ₹{self.balance}")
# get_total_no_accounts(), update_interest_rate()
 
 
class Bank2:
    # Class variable | All your instance share the class variable
    interest_rate = 0.02
 
    def __init__(self, acc_no, name, balance):
        # instance variable
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
 
    def display_balance(self):
        return f"Your balance is: ₹{self.balance:,}"
 
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
 
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"
 
    def apply_interest(self):
        accumulated_interest_amt = self.balance * Bank1.interest_rate
        self.balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"
 
 
sneha = Bank2(128, "Sneha", 1_00_000)
siva = Bank2(129, "Siva", 90_000)
# print(Bank2.get_total_no_accounts())
# print(Bank2.update_interest_rate(0.10))
 
# sneha.apply_interest()
# sneha.display_balance() # 110,000

# Task  5
class SavingsAccount:
    pass
 
 
sabesh = SavingsAccount(131, "Sabesh", 80_000)
 
print(sabesh.apply_interest())  # 5%
print(sabesh.get_balance())
 
 
# Task 6
# withdraw - transaction_fee - 10 Rupee
class CurrentAccount:
    pass
 
   
tanishq = CurrentAccount(132, "Tanishq", 90_000)
 
print(tanishq.withraw(1_000))
print(tanishq.withraw(10_000))
print(tanishq.get_balance())

class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
 
    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"
 
    def __add__(self, other):
        return self.__speed + other.__speed
 
    # Polymorphism:  Method overriding
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu + snowbell)
 
# x = [5, 6, 7]
# print(dir(x))
