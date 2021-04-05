class Project:

    def __init__(self, title,sponsor,project_manager,start_date,end_date,status,id = None):
        self.title = title
        self.sponsor = sponsor
        self.project_manager = project_manager
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.id = id