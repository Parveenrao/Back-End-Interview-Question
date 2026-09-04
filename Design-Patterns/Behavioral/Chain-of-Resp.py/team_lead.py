from leave_approver import LeaverApprover

from leave_request import LeaveRequest


class TeamLead(LeaverApprover):

    MAX_DAYS = 2 

    def approve(self , request : LeaveRequest)-> None:

        if request.days <= self.MAX_DAYS:
            print(f"Team Lead approved"
                  f"{request.days} day(s) leave")

        else:
            print(f"Forwarding to manager")

            self.forward(request)    