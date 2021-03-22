from db.run_sql import run_sql
from models.assignment import Assignment
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def save(assignment):
    sql = "INSERT INTO assignments(description, consultant_id, client_id, days_required) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [assignment.description,assignment.consultant.id,assignment.client.id,assignment.days_required]
    results = run_sql(sql,values)
    assignment.id = results[0]['id']
    return assignment

def select_all():
    assignments = []
    sql = "SELECT * FROM assignments"
    results = run_sql(sql)

    for row in results:
        consultant = consultant_repository.select(row['consultant_id'])
        client = client_repository.select(row['client_id'])
        assignment = Assignment(row['description'],consultant,client,row['days_required'],row['id'])
        assignments.append(assignment)
    return assignments

def select(id):
    assignment = None
    sql = "SELECT * FROM assignments WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    consultant = consultant_repository.select(result['consultant_id'])
    client = client_repository.select(result['client_id'])

    if result is not None:
        assignment = Assignment(result['description'],consultant,client,result['days_required'],result['id'])
    return assignment

def delete_all():
    sql = "DELETE  FROM assignments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM assignments WHERE id = %s"
    values = [id]
    run_sql(sql,values)