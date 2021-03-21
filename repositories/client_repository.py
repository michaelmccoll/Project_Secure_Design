from db.run_sql import run_sql

from models.client import Client
from models.consultant import Consultant
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def save(client):
    sql = "INSERT INTO clients(client_name,type_of_business,consultants_hired) VALUES (%s,%s,%s) RETURNING id"
    values = [client.client_name,client.type_of_business,client.consultants_hired]
    results = run_sql(sql,values)
    client.id = results[0]['id']
    return client

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)

    for row in results:
        # client = client_repository.select(row['client_id'])   # unsure if linked this way
        client = Client(row['client_name'],row['type_of_business'],row['consultants_hired'],row['id'])
        clients.append(client)
    return clients