from db.run_sql import run_sql

from models.consultant import Consultant
from models.client import Client
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def save(consultant):
    sql = "INSERT INTO consultants(name,role,summary,day_rate) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [consultant.name,consultant.role,consultant.summary,consultant.day_rate]
    results = run_sql(sql,values)
    consultant.id = results[0]['id']
    return consultant

def select_all():
    consultants = []
    sql = "SELECT * FROM consultants"
    results = run_sql(sql)

    for row in results:
        consultant = Consultant(row['name'],row['role'],row['summary'],row['day_rate'],row['id'])
        consultants.append(consultant)
    return consultants

def delete_all():
    sql = "DELETE  FROM consultants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM consultants WHERE id = %s"
    values = [id]
    run_sql(sql,values)