my_dict = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

print(my_dict[1:10])
print(my_dict.get(2:20))

my_dict[3:30] = 12
print(my_dict)

my_dict[4:30] = "North-East"
print(my_dict)

my_dict.pop(3:30)
print(my_dict)

print("Address :", my_dict.get("address"))

my_dict.clear()
print(my_dict)