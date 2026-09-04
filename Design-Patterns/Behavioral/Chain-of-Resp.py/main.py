from team_lead import TeamLead
from manager import Manager
from director import Director
from leave_request import LeaveRequest


def build_chain()-> TeamLead:

    team_lead = TeamLead()

    manager = Manager()

    director = Director()


    return team_lead



def main() -> None:

    chain = build_chain()

    requests = [
        LeaveRequest("Parveen", 1, "Personal Work"),
        LeaveRequest("Rahul", 4, "Medical"),
        LeaveRequest("Amit", 15, "Vacation"),
        LeaveRequest("Neha", 500, "World Tour"),
    ]


    for leaves in requests:

        print("-" * 30)

        chain.approve(leaves)

if __name__ == "__main__":
    main()        
