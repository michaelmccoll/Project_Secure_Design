from db.run_sql import run_sql

from models.client import Client
from models.consultant import Consultant
import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

def save(client):
    sql = "INSERT INTO clients(name,type_of_business,contact_details) VALUES (%s,%s,%s) RETURNING id"
    values = [client.name,client.type_of_business,client.contact_details]
    results = run_sql(sql,values)
    client.id = results[0]['id']
    return client

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)

    for row in results:
        client = Client(row['name'],row['type_of_business'],row['contact_details'],row['id'])
        clients.append(client)
    return clients

def delete_all():
    sql = "DELETE  FROM clients"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql,values)