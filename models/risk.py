class Risk:

    def __init__(self, title,description,owner,triage,category,id = None):
        self.title = title
        self.description = description
        self.owner = owner
        self.triage = triage
        self.category = category
        self.id = id