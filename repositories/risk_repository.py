from db.run_sql import run_sql

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.risk_review import RiskReview
from models.control import Control

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository

def save(risk):
    sql = "INSERT INTO risks(title,description,owner,risk_reviews_id,controls_id) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [risk.title,risk.description,risk.owner,risk.risk_reviews.id,risk.controls.id]
    results = run_sql(sql,values)
    risk.id = results[0]['id']
    return risk

def select_all():
    risks = []
    sql = "SELECT * FROM risks"
    results = run_sql(sql)

    for row in results:
        risk_review = "Risks Reviewed Test"
        controls = "Control Test"
        risk = Risk(row['title'],row['description'],row['owner'],risk_review,controls,row['id'])
        risks.append(risk)
    return risks

def select(id):
    risk = None
    sql = "SELECT * FROM risks WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    risk_review = "Risks Reviewed Test"
    controls = "Control Test"

    if result is not None:
        risk = Risk(result['title'],result['description'],result['owner'],risk_review,controls,result['id'])
    return risk

def delete_all():
    sql = "DELETE FROM risks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM risks WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(risk):
    sql = "UPDATE risks SET (title,description,owner,risk_review_id,controls_id) = (%s,%s,%s,%s,%s) WHERE id = %s"
    values = [risk.title,risk.description,risk.owner,risk.risk_review.id,risk.controls.id]
    run_sql(sql,values)

# Find the risks by the consultant = xxx???
# def risks(consultant):
#     values = [consultant.id]
#     sql = f"""
#             SELECT risks.* FROM risks
#             INNER JOIN assignments
#             ON risks.id = assignments.risk_id
#             WHERE consultant_id = %s
#             """
#     results = run_sql(sql,values)
#     risks = []
#     for row in results:
#         risk = risk(row['title'],row['sponsor'],row['risk_manager'],row['start_date'],row['end_date'],row['status'],row['id'])
#         risks.append(risk)
#     return risks
# ----------------------------------------------
# def total_risk_spend():
#     sql = f"""
#             SELECT risk_id, SUM(total_cost) FROM risks
#             INNER JOIN assignments ON risks.id = assignments.risk_id
#             GROUP BY risk_id
#             """
#     total_risk_spend =run_sql(sql)
#     return total_risk_spend