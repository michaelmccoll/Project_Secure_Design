class Triage:

    def __init__(self, project,iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date,id = None):
        self.project = project
        self.iam = iam
        self.infrastructure = infrastructure
        self.supplier = supplier
        self.privacy = privacy
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability
        self.continuity = continuity
        self.date = date
        self.id = id