""" 
=> Template Pattern
    
    -> Define skeleton of an algorithm , and  let subclass override specific steps
    
 
 -> Example , File Processing System 
     
     Same flow for all files 
     1. Read file 
     2. Parse content 
     3. Process content
     4. Save result 
   
    logic different for 
     1. CSV file 
     2. JSON file 
          
"""

from dataclasses import dataclass
from abc import ABC , abstractmethod
from typing import Optional , List , Dict
import logging

logging.basicConfig(level=logging.INFO)

@dataclass
class Result:
    success : bool
    message : str  
    data : Optional[str] = None

# Template Class

class FileProcessor:
    
    def process_file(self, file_path : str) -> Result:
        
        content = self.read(file_path)
        
        if not content:
            return Result(False , "File Empty or not found")
        
        parsed = self.parse(content)
        
        if not parsed:
            return Result(False  , "Parse Failed")
        
        processed  = self.process(parsed)
        
        return self.save(processed)
    
    def read_file(self , file_path : str) -> str:
        logging.info(f"Reading file : {file_path}")
        return "Dummy Data"
    
    @abstractmethod
    def parse(self, content: str):
        pass

    def process(self, data):
        logging.info("Processing data")
        return data

    def save(self, data) -> Result:
        logging.info("Saving result")
        return Result(True, "File processed successfully", data)     

# Concrete Example 

class CSVProcessor(FileProcessor):

    def parse(self, content: str):
        logging.info("Parsing CSV")
        return content.split(",")  # simple simulation    
    
import json

class JSONProcessor(FileProcessor):

    def parse(self, content: str):
        logging.info("Parsing JSON")
        try:
            return json.loads('{"key": "value"}')  # simulate
        except Exception:
            return None    

if __name__ == "__main__":
    csv = CSVProcessor()
    json_p = JSONProcessor()

    print(csv.process_file("data.csv"))
    print(json_p.process_file("data.json"))        