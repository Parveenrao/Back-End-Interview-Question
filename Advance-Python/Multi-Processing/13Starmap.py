"""" 

=> Starmap
    
    -> Is a multi-processing when your function needs multiple function arguemnts
    
    -> map passess one arguments at a time , while starmap send multiple value at a time as separate argments
    
    -> Probblem with map 
       
        def add(a , b):
            return a + b

       -> map cannot do this , map[(1, 2) , (2,3)]

"""


from multiprocessing import Pool

def add(a , b):
    return a + b


if __name__ == "__main__":
    
    values = [(1, 2) , (4 , 5)]
    
    with Pool() as p:
        result = p.starmap(add , values)
    
    print(result)    