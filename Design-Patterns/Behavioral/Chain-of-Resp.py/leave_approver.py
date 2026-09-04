from abc import ABC , abstractmethod

from leave_request import LeaveRequest


class LeaverApprover(ABC):

    def __init__(self) -> None:
        self._next_handler : LeaverApprover | None = None


    def set_next(self, handler : LeaverApprover) -> LeaverApprover:

        # set the next handler and return it

        self._next_handler = handler    

        return handler

    @abstractmethod
    def approve(self , request : LeaveRequest) -> None:
        """ Handle or forware request"""
        ...

    
    def forward(self , request : LeaverApprover) -> None:
        """Forward request to next handler"""

        if self._next_handler:
            self._next_handler.approve(request)

        else:
            print(f"No approver availabe for"
                  f"{request.employee_name}'s request")         