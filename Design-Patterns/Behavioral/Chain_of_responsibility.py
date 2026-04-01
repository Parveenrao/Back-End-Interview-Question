"""   
=> Chain of Responsibility
       -> It passes a request through chain of handlers 
       
       each handler decide
       -> decide to handle it or
          pass it to next handler 
    
    -> Pass request step by step until someont handles it      

=>  File Upload Pipeline 

    1. check file size
    2. check file type 
    3. scan for virus
    4. save file 
  
  -> Any step can reject step
  -> Otherwise it flows forward   

"""

from abc import ABC , abstractmethod
from dataclasses import dataclass
from typing import Dict , List , Optional
import logging

logging.basicConfig(level=logging.INFO)

@dataclass
class Result:
    success : bool   
    message : str   
    data :Optional[str] = None


# base Handler 

class UploadHandler:
    
    def __init__(self):
        self.next = None
    
    def set_next(self , handler):
        self.next = handler
        return handler
    
    @abstractmethod
    def handle(self, file : Dict) -> Result:
        pass
    
    def next(self , file):
        if self.next:
            return self.next.handle(file)
        
        return Result(True , "File Processed")      
    


class FileSizeHandler(UploadHandler):

    def handle(self, file: dict) -> Result:
        if file.get("size", 0) > 5:
            return Result(False, "File too large (max 5MB)")

        logging.info("Size check passed")
        return self.next(file)    

class FileTypeHandler(UploadHandler):

    def handle(self, file: dict) -> Result:
        allowed = ["jpg", "png"]

        if file.get("type") not in allowed:
            return Result(False, "Invalid file type")

        logging.info("Type check passed")
        return self.next(file)    
    
class VirusScanHandler(UploadHandler):

    def handle(self, file: dict) -> Result:
        if file.get("infected"):
            return Result(False, "File contains virus")

        logging.info("Virus scan passed")
        return self.next(file)   
    
class SaveFileHandler(UploadHandler):

    def handle(self, file: dict) -> Result:
        logging.info(f"File saved: {file.get('name')}")
        return Result(True, "Upload successful", {"file": file.get("name")})     

if __name__ == "__main__":
    size = FileSizeHandler()
    ftype = FileTypeHandler()
    virus = VirusScanHandler()
    save = SaveFileHandler()

    # build chain
    size.set_next(ftype).set_next(virus).set_next(save)

    file = {
        "name": "photo.jpg",
        "size": 3,
        "type": "jpg",
        "infected": False
    }

    result = size.handle(file)
    print(result)    