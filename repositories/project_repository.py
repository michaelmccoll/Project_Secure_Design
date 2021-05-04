from db.run_sql import run_sql

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.control import Control

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository

def save(project):
    sql = "INSERT INTO projects(title,sponsor,project_manager,start_date,end_date,status,triage_id) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [project.title,project.sponsor,project.project_manager,project.start_date,project.end_date,project.status,project.triage.id]
    results = run_sql(sql,values)
    project.id = results[0]['id']
    return project

def select_all():
    projects = []
    sql = "SELECT * FROM projects"
    results = run_sql(sql)

    for row in results:
        triage = triage_repository.select(row['triage_id'])
        project = Project(row['title'],row['sponsor'],row['project_manager'],row['start_date'],row['end_date'],row['status'],triage,row['id'])
        projects.append(project)
    return projects

def select(id):
    project = None
    sql = "SELECT * FROM projects WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    triage = triage_repository.select(result['triage_id'])

    if result is not None:
        project = Project(result['title'],result['sponsor'],result['project_manager'],result['start_date'],result['end_date'],result['status'],triage,result['id'])
    return project

def delete_all():
    sql = "DELETE FROM projects"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM projects WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(project):
    sql = "UPDATE projects SET (title,sponsor,project_manager,start_date,end_date,status,triage_id) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [project.title,project.sponsor,project.project_manager,project.start_date,project.end_date,project.status,project.triage.id]
    run_sql(sql,values)

# Find the projects by the consultant = xxx???
# def projects(consultant):
#     values = [consultant.id]
#     sql = f"""
#             SELECT projects.* FROM projects
#             INNER JOIN assignments
#             ON projects.id = assignments.project_id
#             WHERE consultant_id = %s
#             """
#     results = run_sql(sql,values)
#     projects = []
#     for row in results:
#         project = Project(row['title'],row['sponsor'],row['project_manager'],row['start_date'],row['end_date'],row['status'],row['id'])
#         projects.append(project)
#     return projects
# ----------------------------------------------
# def total_project_spend():
#     sql = f"""
#             SELECT project_id, SUM(total_cost) FROM projects
#             INNER JOIN assignments ON projects.id = assignments.project_id
#             GROUP BY project_id
#             """
#     total_project_spend =run_sql(sql)
#     return total_project_spend