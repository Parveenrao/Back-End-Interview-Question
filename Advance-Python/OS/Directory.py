""" 
=> OS With Directory 

"""
import os

# 1. Create Dir 

os.mkdir("data2")

# 2. Create nested Directories 

os.makedirs("a/b/c")

# 3. with exist = ok , prevent crash id dir exist 

os.mkdirs("data1" , "a/b/c")

# 4. Remove directory 

os.rmdir("data")

# 5. Remove nested directories 
  
os.removedirs("a/b/c")