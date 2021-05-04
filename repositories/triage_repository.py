from db.run_sql import run_sql

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.control import Control

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository

def save(triage):
    sql = "INSERT INTO triage(iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date,risks_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [triage.iam,triage.infrastructure,triage.supplier,triage.privacy,triage.confidentiality,triage.integrity,triage.availability,triage.continuity,triage.date,triage.risks.id]
    results = run_sql(sql,values)
    triage.id = results[0]['id']
    return triage

def select_all():
    triages = []
    sql = "SELECT * FROM triage"
    results = run_sql(sql)

    for row in results:
        risk = risk_repository.select(row['risks_id'])
        triage = Triage(row['iam'],row['infrastructure'],row['supplier'],row['privacy'],row['confidentiality'],row['integrity'],row['availability'],row['continuity'],row['date'],risk,row['id'])
        triages.append(triage)
    return triages

def select(id):
    triage = None
    sql = "SELECT * FROM triage WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    risk = risk_repository.select(result['risks_id'])

    if result is not None:
        triage = Triage(result['iam'],result['infrastructure'],result['supplier'],result['privacy'],result['confidentiality'],result['integrity'],result['availability'],result['continuity'],result['date'],risk,result['id'])
    return triage

def delete_all():
    sql = "DELETE FROM triage"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM triage WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(triage):
    sql = "UPDATE triage SET (iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date,risks_id) = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [triage.iam,triage.infrastructure,triage.supplier,triage.privacy,triage.confidentiality,triage.integrity,triage.availability,triage.continuity,triage.date,triage.risks.id]
    run_sql(sql,values)

# Find the triage by the project
def triage(project):
    values = [project.id]
    sql = f"""
            SELECT triage.* FROM triage
            INNER JOIN assignments
            ON triage.id = assignments.triage_id
            WHERE project_id = %s
            """
    results = run_sql(sql,values)
    triage = []
    for row in results:
        risks = risk_repository.select_all()
        triage = Triage(project,row['iam'],row['infrastructure'],row['supplier'],row['privacy'],row['confidentiality'],row['integrity'],row['availability'],row['continuity'],row['date'],risks,row['id'])
        triage.append(triage)
    return triage

# ----------------------------------------------
# def total_triage_spend():
#     sql = f"""
#             SELECT triage_id, SUM(total_cost) FROM triage
#             INNER JOIN assignments ON triage.id = assignments.triage_id
#             GROUP BY triage_id
#             """
#     total_triage_spend =run_sql(sql)
#     return total_triage_spend