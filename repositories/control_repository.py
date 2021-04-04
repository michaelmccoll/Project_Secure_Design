from db.run_sql import run_sql

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.control import Control

import repositories.triage_repository as triage_repository
import repositories.control_repository as control_repository
import repositories.project_repository as project_repository

def save(control):
    sql = "INSERT INTO controls(title,description,owner) VALUES (%s,%s,%s) RETURNING id"
    values = [control.title,control.description,control.owner]
    results = run_sql(sql,values)
    control.id = results[0]['id']
    return control

def select_all():
    controls = []
    sql = "SELECT * FROM controls"
    results = run_sql(sql)

    for row in results:
        control = Control(row['title'],row['description'],row['owner'],row['id'])
        controls.append(control)
    return controls

def select(id):
    control = None
    sql = "SELECT * FROM controls WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        control = Control(row['title'],row['description'],row['owner'],row['id'])
    return control

def delete_all():
    sql = "DELETE FROM controls"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM controls WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(control):
    sql = "UPDATE controls SET (title,description,owner) = (%s,%s,%s) WHERE id = %s"
    values = [control.title,control.description,control.owner]
    run_sql(sql,values)

# Find the controls by the consultant = xxx???
# def controls(consultant):
#     values = [consultant.id]
#     sql = f"""
#             SELECT controls.* FROM controls
#             INNER JOIN assignments
#             ON controls.id = assignments.control_id
#             WHERE consultant_id = %s
#             """
#     results = run_sql(sql,values)
#     controls = []
#     for row in results:
#         control = control(row['title'],row['sponsor'],row['control_manager'],row['start_date'],row['end_date'],row['status'],row['id'])
#         controls.append(control)
#     return controls
# ----------------------------------------------
# def total_control_spend():
#     sql = f"""
#             SELECT control_id, SUM(total_cost) FROM controls
#             INNER JOIN assignments ON controls.id = assignments.control_id
#             GROUP BY control_id
#             """
#     total_control_spend =run_sql(sql)
#     return total_control_spend