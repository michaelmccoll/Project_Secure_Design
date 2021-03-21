import pdb
from models.consultant import Consultant
from models.client import Client
from models.assignment import Assignment

import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

# Consultant(consultant_name, role, summary, day_rate)
# Client(client_name, type_of_business, consultants_hired)
# Consultant(consultant, client, days_required)

pdb.set_trace()