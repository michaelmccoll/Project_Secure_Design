import pdb
from models.consultant import Consultant
from models.client import Client
from models.assignment import Assignment

import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

assignment_repository.delete_all()
client_repository.delete_all()
consultant_repository.delete_all()

### Consultant(consultant_name,role,summary,day_rate) ###
consultant1 = Consultant('Michael McColl','Director','Risk and security consultant',400)
consultant_repository.save(consultant1)
consultant2 = Consultant('John Smith','Analyst','IT analyst',300)
consultant_repository.save(consultant2)
consultant3 = Consultant('Angela Black','Manager','Website designer',500)
consultant_repository.save(consultant3)
consultant4 = Consultant('George Jones','Manager','Backend software developer',450)
consultant_repository.save(consultant4)
consultant5 = Consultant('Murray Irvine','Senior Manager','Mobile application architect',550)
consultant_repository.save(consultant5)

### Client(client_name,type_of_business,consultants_hired) ###
client1 = Client('Lloyds Banking Group','Financial Services','bob_anderson@lbg.co.uk')
client_repository.save(client1)
client2 = Client('AirBNB','Hospitality','sourcing@airbnb.com')
client_repository.save(client2)
client3 = Client('Apple','IT','apple_hr@apple.com')
client_repository.save(client3)

### Assignment(consultant, client, days_required) ###
assignment1 = Assignment(consultant1,client1,10)
assignment_repository.save(assignment1)
assignment2 = Assignment(consultant2,client2,20)
assignment_repository.save(assignment2)
assignment3 = Assignment(consultant4,client3,30)
assignment_repository.save(assignment3)

pdb.set_trace()