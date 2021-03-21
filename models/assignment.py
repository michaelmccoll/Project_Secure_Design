class Assignment:

    def __init__(self, consultant, client, days_required, id = None):
        self.consultant = consultant
        self.client = client
        self.days_required = days_required
        self.id = id

# EXTENTIONS:
# May need a 'status' variable, to show when an assignment is completed, so it can be rated.
# May need a 'rating' variable, so client can rate the consultants assignment.