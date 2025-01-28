import os
os.system('cls' if os.name == 'nt' else 'clear')

myfamily = ("mother", "father", "sister", "brother", "sister")

print("Type of myfamily:", type(myfamily)) 

print("First sister:", myfamily[2])  
print("Second sister:", myfamily[4]) 

try:
    myfamily.append("me") 
except AttributeError as e:
    print("Error:", e) 

try:
    myfamily.pop(3) 
except AttributeError as e:
    print("Error:", e) 