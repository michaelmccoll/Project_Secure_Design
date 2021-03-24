import pdb
from models.consultant import Consultant
from models.client import Client
from models.assignment import Assignment
from models.admin import Admin

import repositories.consultant_repository as consultant_repository
import repositories.client_repository as client_repository
import repositories.assignment_repository as assignment_repository

assignment_repository.delete_all()
client_repository.delete_all()
consultant_repository.delete_all()

### Consultant(consultant_name,role,summary,day_rate) ###
consultant1 = Consultant('Michael McColl','Director','IT risk and security consultant',500)
consultant_repository.save(consultant1)
consultant2 = Consultant('John Smith','Analyst','IT analyst',300)
consultant_repository.save(consultant2)
consultant3 = Consultant('Angela Black','Manager','Website designer',500)
consultant_repository.save(consultant3)
consultant4 = Consultant('George Jones','Manager','Data analytics analyst',450)
consultant_repository.save(consultant4)
consultant5 = Consultant('Murray Irvine','Senior Manager','Mobile application architect',550)
consultant_repository.save(consultant5)
consultant6 = Consultant('Rick Edinburgh','Director','Mobile app game designer',450)
consultant_repository.save(consultant6)
consultant7 = Consultant('Murray Irvine','Senior Manager','Backend software developer',550)
consultant_repository.save(consultant7)
consultant8 = Consultant('Thomas Baxter','Analyst','Mobile application architect',550)
consultant_repository.save(consultant8)
consultant9 = Consultant('Joyce Blue','Manager','Frontend developer',350)
consultant_repository.save(consultant9)
consultant10 = Consultant('Bobby Morgan','Analyst','Data analytics analyst',450)
consultant_repository.save(consultant10)

### Client(client_name,type_of_business,consultants_hired) ###
client1 = Client('Lloyds Banking Group','Financial Services','steve_anderson@lbg.co.uk')
client_repository.save(client1)
client2 = Client('AirBNB','Hospitality','sourcing@airbnb.com')
client_repository.save(client2)
client3 = Client('Apple','IT','apple_hr@apple.com')
client_repository.save(client3)
client4 = Client('Microsoft','IT','info@microsoft.co.uk')
client_repository.save(client4)
client5 = Client('Sky News','Media','resourcing@skynews.com')
client_repository.save(client5)
client6 = Client('Argos','Retail','it_operations@argos.co.uk')
client_repository.save(client6)
client7 = Client('Hilton','Hospitality','procurement@hilton.com')
client_repository.save(client7)
client8 = Client('Starling Bank','Financial Services','it_sourcing@starling.co.uk')
client_repository.save(client8)

### Assignment(consultant, client, days_required, start_date, end_date, total_cost) ###
assignment1 = Assignment("Create a web app",consultant1,client1,10,"2021-01-01","2021-01-21",5000)
assignment_repository.save(assignment1)
assignment2 = Assignment("Develop some backend code",consultant2,client2,20,"2021-01-27","2021-02-10",6000)
assignment_repository.save(assignment2)
assignment3 = Assignment("Design a new UX frontend",consultant3,client3,30,"2021-02-09","2021-03-15",15000)
assignment_repository.save(assignment3)
assignment4 = Assignment("Conduct some data analytics",consultant4,client4,5,"2021-02-22","2021-02-28",2250)
assignment_repository.save(assignment4)
assignment5 = Assignment("Design new wireframes for app",consultant6,client5,15,"2021-01-05","2021-03-25",6750)
assignment_repository.save(assignment5)
assignment6 = Assignment("Write some new API's for app",consultant5,client6,20,"2021-03-04","2021-03-26",11000)
assignment_repository.save(assignment6)
assignment7 = Assignment("Refresh the UX frontend",consultant7,client7,35,"2021-04-01","2021-05-16",19250)
assignment_repository.save(assignment7)
assignment8 = Assignment("Create an IT strategy & roadmap",consultant1,client2,50,"2021-04-01","2021-06-21",25000)
assignment_repository.save(assignment8)
assignment9 = Assignment("Conduct some data analytics",consultant2,client1,10,"2021-02-11","2021-03-17",3000)
assignment_repository.save(assignment9)
assignment10 = Assignment("Conduct some data analytics",consultant4,client7,5,"2021-01-23","2021-01-29",2250)
assignment_repository.save(assignment10)
assignment11 = Assignment("Write data analytics plan",consultant4,client7,20,"2021-03-04","2021-04-07",9000)
assignment_repository.save(assignment11)
assignment12 = Assignment("Integrate new API's",consultant2,client3,15,"2021-03-28","2021-04-19",4500)
assignment_repository.save(assignment12)

# To test view controllers and styling:
# Consultant10 will have no assingments or clients
# Client8 will have no assignments or consultants
# Assignments cannot be created without a client and consultant

pdb.set_trace()