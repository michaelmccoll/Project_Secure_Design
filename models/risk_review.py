class RiskReview:

    def __init__(self, inherrent_likelihood,inherrent_impact,residual_likelihood,residual_impact,date,id=None):
        self.inherrent_likelihood = inherrent_likelihood
        self.inherrent_impact = inherrent_impact
        self.residual_likelihood = residual_likelihood
        self.residual_impact = residual_impact
        self.date = date
        self.id = id

# These would always be auto-calculated variables, so not needed in Class setup above
    # def inherrent_rating():
    #     inherrent_likelihood * inherrent_impact

    # def residual_rating():
    #     residual_likelihood * residual_impact