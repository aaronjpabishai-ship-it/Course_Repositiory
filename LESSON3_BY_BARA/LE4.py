#Measure Distance
print(abs(2 - 9)) #returns the absolute values of the sum (non-negative)

# Round Numbers : math.floor(x) lowest |  math.ceil(x) highest | round(x) always use #import
# math.trunc(x) strictly remove decimal


import math
price = 27.954263
print(round(price))
print(round(price, 2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

#can also use
print(int(price))