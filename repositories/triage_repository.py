from db.run_sql import run_sql

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.control import Control
from models.categories import Category

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository
import repositories.category_repository as category_repository

def save(triage):
    sql = "INSERT INTO triage(question,project_id,category_id,date) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [triage.question,triage.project.id,triage.category.id,triage.date]
    results = run_sql(sql,values)
    triage.id = results[0]['id']
    return triage

def select_all():
    triages = []
    sql = "SELECT * FROM triage"
    results = run_sql(sql)

    for row in results:
        project = project_repository.select(row['project_id'])
        category = category_repository.select(row['category_id'])
        triage = Triage(row['question'],project,category,row['id'])
        triages.append(triage)
    return triages

def select(id):
    triage = None
    sql = "SELECT * FROM triage WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    project = project_repository.select(result['project_id'])
    category = category_repository.select(result['category_id'])

    if result is not None:
        triage = Triage(result['question'],project,category,result['id'])
    return triage

def delete_all():
    sql = "DELETE FROM triage"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM triage WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(triage):
    sql = "UPDATE triage SET (question,project_id,category_id,date) = (%s,%s,%s,%s) WHERE id = %s"
    values = [triage.question,triage.project.id,triage.category.id,triage.date]
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
        category = category_repository.select_all()
        triage = Triage(row['question'],project,category,row['date'],row['id'])
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