# Leave request model 

from dataclasses import dataclass

@dataclass(slots=True)
class LeaveRequest:
    employee_name : str 
    days : int 
    reason : str

    