""" 


=> Sorting

   -> Filter decide which records to return , sorting decide in what order those records 
      should return


      GET/product?category=Laptop&sort=price

=> Why sort 

    1. Lowest price first 
    2. Highest price first 
    3. Newest product first 
    4. best-rated peoduct first 
    5. Most popular first 



=> query

    query.where(product.price.asc())


=> Dynamic Sorting


    query = select(user)

    if sort == "price":
        query.order_by(Product.price.asc())

    if sort == "rating":
        query.order_by(product.price.desc())
                 



"""