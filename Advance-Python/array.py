"""

=> Pack and Unpacking In arrays



=> 1. Packing In List 

       -> Put multiple values in single list

       numbers = [10 ,20 ,40]

       print(numbers)
"""

# Unpacking a list 
nubmers = [10, 20, 30]

a , b , c = nubmers        # rule the no. of variable must match the number of elements

print(a)
print(b)
print(c)


# Star (*) Unpacking , python allow one variable to collect the remaining elements

a , *b = [10 ,20, 30, 40]

print(a)

print(b)

*a , b = [1, 2, 3, 4]

# middle unpacking 

a , *middle , b = [1, 2, 3, 4 ,5]

print(a)

print(middle)

print(b)

# Ignoring values 

a , _ , c = [1, 2, 3]    # a = 1, c = 3


# nested unpacking 

data = [1, [2, 3]]

a, (b,c) = data

print(a)

print(b)

print(c)


# combine multiple list 


x = [1, 2, 3]

y = [4, 5, 6]

z = [*x , *y]

print(z)
