from db.run_sql import run_sql
from models.consultant import Consultant
from models.client import Client
from models.assignment import Assignment
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def assignment_stats():
    assignments = []
    sql = "SELECT * FROM assignments"
    results = run_sql(sql)

    for row in results:
        consultant = consultant_repository.select(row['consultant_id'])
        client = client_repository.select(row['client_id'])
        assignment = Assignment(row['description'],consultant,client,row['days_required'],row['start_date'],row['end_date'],row['total_cost'],row['id'])
        assignments.append(assignment)
    return assignments

# def select_all():
#     assignments = []
#     sql = "SELECT * FROM assignments"
#     results = run_sql(sql)

#     for row in results:
#         consultant = consultant_repository.select(row['consultant_id'])
#         client = client_repository.select(row['client_id'])
#         assignment = Assignment(row['description'],consultant,client,row['days_required'],row['start_date'],row['end_date'],row['total_cost'],row['id'])
#         assignments.append(assignment)
#     return assignments