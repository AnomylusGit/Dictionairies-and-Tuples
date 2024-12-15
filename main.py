my_dict = {"name": "Aarush", "age": 11}

print(my_dict["name"])
print(my_dict.get("age"))

my_dict["age"] = 12
print(my_dict)

my_dict["address"] = "North-East"
print(my_dict)

my_dict.pop("age")
print(my_dict)

print("Address :", my_dict.get("address"))

my_dict.clear()
print(my_dict)