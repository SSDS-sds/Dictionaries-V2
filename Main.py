#Creating a dictionary
animals = {"Hamster":"Milktea","Dog":"Mely","Bird":"Sparrow"}
print(animals)

#Acessing values from a dictionary
my_bird = animals["Bird"]
print(f"My pet bird's name is {my_bird}")

#Creating a list of keys
keys_list = list(animals.keys())
print(keys_list)

#Creating a list of values
values_list = list(animals.values())
print(values_list)

#Looping through the keys of the dictionary
for key in animals:
    print(key)

#Accessing the values of the dictionary
for value in animals:
    print(animals[value])

#Checking for a key in a dictionary
if "Cat" in animals:
    print("It is a key")
else:
    print("It is not a key")

#Adding key, value pairs to dictionary
animals["Cat"] = "Pudge"
print(animals)

#Deleting a key, value, pair from a dictionary
del(animals["Dog"])
print(animals)

#Changing a value in a dictionary
animals["Cat"] = "Fluffy"
print(animals)

#Create a new key with a list of values
animals["Snake"] = ["Squishy","Slytherin","Basalisk"]
print(animals)

#Accessing values from lists in dicxtionaries
my_house = animals["Snake"][1]
print(f"I am from the house of {my_house}. ")