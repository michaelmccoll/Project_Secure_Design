from db.run_sql import run_sql
from models.assignment import Assignment
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def save(assignment):
    sql = "INSERT INTO assignments(consultant, client, days_required) VALUES (%s,%s,%s) RETURNING id"
    values = [assignment.consultant.id,assignment.client.id,assignment.days_required]
    results = run_sql(sql,values)
    assignment.id = results[0]['id']
    return assignment

def select_all():
    assignments = []
    sql = "SELECT * FROM assignments"
    results = run_sql(sql)

    for row in results:
        # client = client_repository.select(row['client_id'])   # unsure if linked this way
        assignment = Assignment(row['consultant'],row,['client'],row['days_required'],row['id'])
        assignments.append(assignment)
    return assignments