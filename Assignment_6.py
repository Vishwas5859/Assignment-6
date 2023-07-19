# Assignment-6: JSON and OOP Assignment
# Assignment-1, Ques-1

# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State. Write a python program 
# that reads this information from the JSON file and saves the information into a list of 
# objects of Employee class. Finally print the list of the Employee objects.

# JSON file:-
{
"Employees" : [
{
"name":"Mike",
"DOB":"12-01-1985",
"height":"1.3m",
"city":"Hydrabad",
"state": "Telangana"
},
{
"name":"Raj",
"DOB":"22-03-1985",
"height":"1.6m",
"city":"Bangalore",
"state": "Karnataka"
},
{
"name":"Suraj",
"DOB":"16-02-1985",
"height":"1.55m",
"city":"Cochi",
"state": "Kerala"
},
{
"name":"Anmol",
"DOB":"28-07-1985",
"height":"1.75m",
"city":"Kolkata",
"state": "West Bengal"    
},
{
"name":"Randeep",
"DOB":"17-04-1985",
"height":"1.64m",
"city":"Ahmedabad",
"state": "Gujarat" 
}
]
}

# Python Code:

import json
f = open('employee.json')
data = json.load(f)
for i in data['Employees']:
    print(i)
  
f.close()

# output:-
{'name': 'Mike', 'DOB': '12-01-1985', 'height': '1.3m', 'city': 'Hydrabad', 'state': 'Telangana'}
{'name': 'Raj', 'DOB': '22-03-1985', 'height': '1.6m', 'city': 'Bangalore', 'state': 'Karnataka'}
{'name': 'Suraj', 'DOB': '16-02-1985', 'height': '1.55m', 'city': 'Cochi', 'state': 'Kerala'}
{'name': 'Anmol', 'DOB': '28-07-1985', 'height': '1.75m', 'city': 'Kolkata', 'state': 'West Bengal'}
{'name': 'Randeep', 'DOB': '17-04-1985', 'height': '1.64m', 'city': 'Ahmedabad', 'state': 'Gujarat'}
#------------------------------------------------------------------------------------------------------------

# QUES 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
dict1 = {"Uttar Pradesh":"Lucknow","Karnataka": "Bangalore","Tamil Nadu":"Chennai",
         "Manipur":"Imphal","Rajasthan":"Jaipur","Haryana":"Chandigarh","Goa":"Panaji"}

json_obj = json.dumps(dict1,indent=4)
print(json_obj)

# Output:-
{
    "Uttar Pradesh": "Lucknow",
    "Karnataka": "Bangalore",
    "Tamil Nadu": "Chennai",
    "Manipur": "Imphal",
    "Rajasthan": "Jaipur",
    "Haryana": "Chandigarh",
    "Goa": "Panaji"
}
#------------------------------------------------------------------------------------------------------

# Assignment 2 -Create a class named ‘Dog’. It should have a constructor 
#which accepts its name, age and coat color

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’.
# It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour
    
    def description(self):
        return f"name of the dog is: {self.name}, Age of the Dog is: {self.age}"

    def get_info(self):
        return f"The coat colour of the Dog is: {self.colour}"
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, colour, weight, breed):
        Dog.__init__(self, name, age,colour)
        self.weight = weight
        self.breed = breed

    def get_weight(self):
        return f"The weight of Dog is: {self.weight}"
    
    def get_breed(self):
        return f"The breed of the dog is: {self.breed}"

class Bulldog(Dog):
    def __init__(self, name, age, colour,city, owner_name):
        Dog.__init__(self,name,age,colour)
        self.city = city
        self.owner_name = owner_name

    def get_address(self):
        return f"The dog is in: {self.city}"

    def get_owner(self):
        return f"The owner of the dog is: {self.owner_name}"

obj1 = Dog("Jimmy","2.5","White")
print(obj1.description())
print(obj1.get_info())

obj2 = JackRussellTerrier("Scooby","2.5","light brown","7.2 Kgs","Lab")
print(obj2.description())
print(obj2.get_weight())
print(obj2.get_info())
print(obj2.get_breed())

obj3 = Bulldog("Bruno","3","white and brown","Bangalore","Big Mike")
print(obj3.description())
print(obj3.get_info())
print(obj3.get_owner())
print(obj3.get_address())