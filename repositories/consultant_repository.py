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

def select(id):
    consultant = None
    sql = "SELECT * FROM consultants WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        consultant = Consultant(result['name'],result['role'],result['summary'],result['day_rate'],result['id'])
    return consultant

def delete_all():
    sql = "DELETE  FROM consultants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM consultants WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# Find which consultants are assigned to clients
def consultants(client):
    values = [client.id]
    sql = f"""
            SELECT consultants.* FROM consultants
            INNER JOIN assignments
            ON consultants.id = assignments.consultant_id
            WHERE client_id = %s
            """
    results = run_sql(sql,values)
    consultants = []
    for row in results:
        consultant = Consultant(row['name'],row['role'],row['summary'],row['day_rate'], row['id'])
        consultants.append(consultant)
    return consultants