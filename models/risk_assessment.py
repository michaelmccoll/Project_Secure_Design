class RiskAssessment:

    def __init__(self, inherrent_likelihood,inherrent_impact,residual_likelihood,residual_impact,risk_review_date):
        self.inherrent_likelihood = inherrent_likelihood
        self.inherrent_impact = inherrent_impact
        self.residual_likelihood = residual_likelihood
        self.residual_impact = residual_impact
        self.risk_review_date = risk_review_date

# These would always be auto-calculated variables, so not needed in Class setup above
    # def inherrent_rating():
    #     inherrent_likelihood * inherrent_impact

    # def residual_rating():
    #     residual_likelihood * residual_impact