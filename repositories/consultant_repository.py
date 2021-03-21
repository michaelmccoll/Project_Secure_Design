from db.run_sql import run_sql

from models.consultant import Consultant
from models.client import Client
import repositories.client_repository as client_repository

def select_all():
    consultants = []
    sql = "SELECT * FROM consultants"
    results = run_sql(sql)

    for row in results:
        # client = client_repository.select(row['client_id'])   # unsure if linked this way
        consultant = Consultant(row['name'],row['id'])
        consultants.append(consultant)
    return consultants