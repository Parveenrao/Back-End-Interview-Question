""" 

=> Filtering 


     -> Filtering means return only the data that matches certain condition


     -> without filtering 

         GET/users

           -> return all user 

     -> with filtering 

         we want users who are admins 

            GET/user?role=admin

     -> multiple filters


         GET/users?role=Admin&city=Delhi



=> Numeric Filtering 

    -> GET/products?price = 5000

=> Range Filter

    GET/products?min_price=50000


=> Date Filter

    -> Order after a certain date

        GET/orders?created_after = 2025-01-01

=> Boolean Filter 

    GET/users!active = true

=> IN Filter 


    GET/products?category = Laptop,Phone


=> Combining everything 


    GET/products?category = Laptop&min_price=5000&max_price= 12000&brand = dell


    query = select(Product)

    if category:
         query.where(Product.category == category)

    if min_price:
        query.where(Product.min_price >=min_price)

    if max_price:
        query.where(Product.max_price <= max_price)

    if brand:
        quer.where(Product.brand = brand)      


=> from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/products")
def get_products(
    category: str | None = None,
    brand: str | None = None,
    min_price: int | None = None,
    max_price: int | None = None,
    db: Session = Depends(get_db),
):
    query = select(Product)

    if category:
        query = query.where(Product.category == category)

    if brand:
        query = query.where(Product.brand == brand)

    if min_price is not None:
        query = query.where(Product.price >= min_price)

    if max_price is not None:
        query = query.where(Product.price <= max_price)

    products = db.execute(query).scalars().all()

    return products             



=> Best Practices  
          Keep filters in query parameters, not the URL path.
          Make filters optional unless they're required by the business logic.
          Combine filtering with pagination to avoid returning huge result sets.
          Validate query parameter types (e.g., int, bool, date) using FastAPI.
          Build queries incrementally so only the requested filters are applied.          












"""