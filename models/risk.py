class Risk:

    def __init__(self, title,description,owner,risk_reviews = None,controls = None,id = None):
        self.title = title
        self.description = description
        self.owner = owner
        self.risk_reviews = risk_reviews
        self.controls = controls
        self.id = id