class Triage:

    def __init__(self, iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date,risks = None,id = None):
        self.iam = iam
        self.infrastructure = infrastructure
        self.supplier = supplier
        self.privacy = privacy
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability
        self.continuity = continuity
        self.date = date
        self.risks = risks
        self.id = id