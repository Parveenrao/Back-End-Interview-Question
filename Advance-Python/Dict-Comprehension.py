"""  
=> Dictionary Comprehension is a compact way to create dictionary using single line of code 
     
     {key : value  for item in iterable }

"""

# Square odd numbers using normal and dict comprehension 

d = {}

for i in range(5):
    d[i] = i * i

print(d)    

# Now dict comprehension 

d1 = {i : i* i for i in range(10)}

print(d1)


#-----------------------------------------------------------------------------------------

# Square only odd number

s = {}

for i in range(1 , 11):
    if i % 2 != 0:
        
        s[i] = i*i

print(s)


s3 = {i*i for i in range(1 , 11) if i %2 != 0}

print(s3)

#----------------------------------------------------------------------------------------------

# Cube only odd numbers 

e = {}

for i in range(1, 11):
    if i % 2!= 0:
        e[i] = i**3

print(e)        


e1 = {i: i**3 for i in range(10) if i % 2 != 0}


print(e1)        
