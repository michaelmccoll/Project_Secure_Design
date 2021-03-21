from db.run_sql import run_sql

from models.client import Client
from models.consultant import Consultant
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)

    for row in results:
        # client = client_repository.select(row['client_id'])   # unsure if linked this way
        client = Client(row['client_name'],row['type_of_business'],row['consultants_hired'],row['id'])
        clients.append(client)
    return clients