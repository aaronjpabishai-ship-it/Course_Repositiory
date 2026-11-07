#is integer to check if there is an inteher

# x = 7.0
# print (x.is_integer())

# y = 7.7
# print(y.is_integer())


# #isinstance

# x = 70.4
# print(isinstance(x,int))
# print(isinstance(x,float))

#PYTHON CHALLENGE
#Generate a random integer between 1 to 100 and check if the result is an even number/


import random
# x = 1
# y = 100
a = random.randint(1, 100)
print(a)
print(a % 2 == 0)