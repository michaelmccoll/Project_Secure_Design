class Assignment:

    def __init__(self, description, consultant, client, days_required, start_date = None, end_date = None, total_cost = None, id = None):
        self.description = description
        self.consultant = consultant
        self.client = client
        self.days_required = days_required
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
        self.id = id


    @classmethod
    def calculate_costs(cls,consultant_day_rate,assignment_days):
        return int(consultant_day_rate) * int(assignment_days)
    

# EXTENTIONS:
# May need a 'status' variable, to show when an assignment is completed, so it can be rated.
# May need a 'rating' variable, so client can rate the consultants assignment.