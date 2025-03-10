#Excercise
date = input("Enter today's date: ")
mood = input("How would you rate your mood today on a scale of 1-10? \n")
journal = input("Write your thoughts here \n")

with open("Journal.txt","w") as file:
    file.write(mood)
    file.write(journal)



# #Excercise 2:
languages = ['English', 'German', 'Spanish']
for i in languages:
    with open(f"{i}.txt","w") as file:
        file.write(i)


# #Excercise 3:
with open("story.txt","r") as file:
    content = file.read()
    
with open("story_copy.txt","w") as file:
    file.write(content)

# #Excercise 4:
with open("file.txt", 'r') as file:
    content = file.read()

print(content)
print(len(content))

#Excercise 5:
#Write a program that checks if a password set up is strong enough:
#conditions:
#1. > 8 chars
#2. atleast 1 digit
#3. atleast 1 uppercase letter

password = input("Enter the password: \n")

result = {}

if len(password)>=8:
    result["length"]=True
else:
    result["length"]=False
digit = False

for i in password:
    if i.isdigit():
        digit = True
result["digits"]=digit

upperc=False
for i in password:
    if i.isupper():
        upperc = True
result["uppercase"]=upperc



if all(result.values())== True:
    print("Strong Password")

else:
    print("Weak password")


#Excercise:

passw= input("Enter a new password: ")
 
if len(passw) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")


#Excercise:

password = input("Enter a new password: ")
 

if len(password) > 7:
    print("Great password there")
elif len(password)==7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")


#Excercise:
day_temperatures = {"morning":20.5,"noon":10.8,"evening":12.6}

#Excercise:
day_temperatures={"morning":(10.2,1.3,8.2) ,"noon":(1.3,2.6,3.5) ,"evening":(1.2,9.0,2.4)}

#Excercise:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

#Excercise:
ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)

#Excercise:

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)

#Excercise:

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")

#Excercise:

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ZeroDivisionError:
    print("You need to enter a number. Run the program again.")


#Excercise

colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color>50:
        print(color)

#Excercise

passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]
for p in passwords:
    if len(p)<8:
        print(p)

#Excercise

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for i in filenames:
    print(i[:-4])

#Excercise

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for i in filenames:
    print(i[:-4].capitalize())


#Excercise:

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return (f"Max: {maximum}, Min: {minimum}")
    
print(get_max())


#Excercise:

def format_filename():
    filename="report.txt"
    cut = filename[:-4].capitalize()
    return cut


print(format_filename())


#Excercise:

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum
    
celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)

#Excercise:

def strength(password):
    lenp = False
    result=[]
    if len(password) >= 8:
        lenp = True
    result.append(lenp)
    up= False
    for i in password:
        if i.isupper():
            up = True
    result.append(up)
    
    dig = False
    for i in password:
        if i.isdigit():
            dig= True
        
    result.append(dig)
    
    if all(result):
        output= "Strong Password"
    else:
        output = "Weak Password"
        
    return output
      
    
#Excercise

def get_nr_items(one):
    spl=one.split(",")
    l=len(spl)
    return l

#Excercise


FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"



