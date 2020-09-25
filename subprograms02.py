def getName ():
  name = str(input("Enter first name >>>"))
  return name

def getAge():
  age = int(input("Enter your age >>>"))
  return age
  
def welcome_name (name):
  print("Hello", name)
  
def welcome_age (age):
  print("You are", age, "years old")
  
def start():
  first_name = getName()
  welcome_name (first_name)
  ageCheck = getAge()
  welcome_age (ageCheck)
def login():
  last_name=input("last name pls")
  username=input("user name")
  passcode=int(input("input passcode pin"))
  print(last_name,username,passcode)
login()
start()
