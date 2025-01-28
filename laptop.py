import os
os.system('cls' if os.name == 'nt' else 'clear')

laptop = {"brand": "dell", "model": "alienware", "year": 2010}

print("Brand:", laptop["brand"]) 

laptop["home"] = True  
print("Updated dictionary:", laptop)  

laptop["year"] = 2019  
print("Modified dictionary:", laptop)  