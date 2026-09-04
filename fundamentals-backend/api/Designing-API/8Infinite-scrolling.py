""" 


=> Infinite Scrolling 

    -> Infinite scrolling is a UI pattern where new data loads automatically as the user reaches
       the bottom of the page , instead of clicking "Next" or page numbers


=> Infinite scrolling is a user interface pattern where additional content is 
   automatically loaded as the user scrolls instead of using page numbers or a "Next" button. 
   It is typically implemented using keyset (cursor) pagination, 
   where each API response includes a cursor pointing to the last item returned. 
   The frontend sends that cursor in the next request, allowing the backend to efficiently 
   fetch the next batch of records using indexed queries like WHERE id > last_id LIMIT 20. 
   This scales much better than offset-based pagination for large datasets.       



"""