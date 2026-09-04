""" 

=> Searching 

   -> Searching means finding records that contain a given word or phrase


   query = select(product)

   if search:
       query = query.where(
               Product.name.ilike(f%{search}%))

               
   -> search multiple columns 

        query.where(or_(Product.name.ilike(f%{search}%),
                        Product.description.ilike(f%{search}%)))     



=> search three columns 

query = query.where(
    or_(
        Product.name.ilike(f"%{search}%"),
        Product.description.ilike(f"%{search}%"),
        Product.brand.ilike(f"%{search}%")
    )
)



=> sorting + filtering

     select * from products 
     where category = laptop

     and (name like = %dell%
         or description like %dell%)

=> searching + filtering + sorting 

    SELECT *
FROM products
WHERE category='Laptop'
AND (
name ILIKE '%dell%'
OR description ILIKE '%dell%'
)
ORDER BY price DESC;



=> example 
     from sqlalchemy import select, or_

@router.get("/products")
def get_products(
    category: str | None = None,
    search: str | None = None,
):

    query = select(Product)

    if category:
        query = query.where(
            Product.category == category
        )

    if search:
        query = query.where(
            or_(
                Product.name.ilike(f"%{search}%"),
                Product.description.ilike(f"%{search}%"),
                Product.brand.ilike(f"%{search}%")
            )
        )

    return db.execute(query).scalars().all()
"""
