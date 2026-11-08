# Immutable objects (int)
x = 5
y = x

print("Memory address of object x is: " + str(id(x)))
print("Memory address of object y is: " + str(id(y)))
print("Are objects identical? " + str(str(x is y)))

x += 1
print("Memory address of object x incremented by one is: " + str(id(x)))


# Mutable object

my_list = [1, 2, 3]
print("Memory address of object my_list is: " + str(id(my_list)))

my_list.append(4)
print("Memory address of object my_list after adding an extra element is: " + str(id(my_list)))


# PyInterning and pyOptimization

x = 20
y = 19 + 1
print("Are objects identical? " + str(str(x is y)))

s1 = "Python!"
print("Memory address of object s1 is: " + str(id(s1)))
s2 = "Python!"
print("Memory address of object s2 is: " + str(id(s2)))
print("Are objects identical? " + str(str(s1 is s2)))