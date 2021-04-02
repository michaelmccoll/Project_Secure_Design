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

### Project(title,sponsor,project_manager,start_date,end_date,status) ###
project1 = Project('Project Black','Pete Smith','Joe Jones','2021-03-01','2021-10-01','Testing')
project_repository.save(project1)
project2 = Project('Project White','Harry Stones','Gemma Edinburgh','2021-03-01','2021-10-01','Development')
project_repository.save(project2)
project3 = Project('Project Blue','John James','Joe Jones','2021-03-01','2021-10-01','Not Started')
project_repository.save(project3)
project4 = Project('Project Pink','Murray Vegas','Jane Glasgow','2021-03-01','2021-10-01','Planning')
project_repository.save(project4)
project5 = Project('Project Orange','Laura London','Mark Arkus','2021-03-01','2021-10-01','Design Phase')
project_repository.save(project5)

### Triage(question) ###
triage1 = Triage('Is the project implementing or changing any Identity & Access Managment methods?')
triage_repository.save(triage1)
triage2 = Triage('Is the project implementing or changing any Infrastructure')
triage_repository.save(triage2)
triage3 = Triage('Is the project implementing or changing any Supplier Relationships?')
triage_repository.save(triage3)
triage4 = Triage('Is the project implementing or changing any Personally Identifiable Information?')
triage_repository.save(triage4)
triage5 = Triage('What is the Confidentiality rating of information involved?')
triage_repository.save(triage5)
triage6 = Triage('What is the Integrity rating of information involved?')
triage_repository.save(triage6)
triage7 = Triage('What is the Availability rating of information involved?')
triage_repository.save(triage7)
triage8 = Triage('What is the highest Business Continuity rating of the processes involved?')
triage_repository.save(triage8)

### Risk(title,description,owner) ###
risk1 = Risk('Identity & Access Management risk','IAM blah blah blah','Steve Smith')
risk_repository.save(risk1)
risk2 = Risk('Infrastrucrure risk','Infrastructure blah blah blah','Steve Smith')
risk_repository.save(risk2)
risk3 = Risk('Supplier risk','Supplier blah blah blah','Steve Smith')
risk_repository.save(risk3)
risk4 = Risk('GDPR risk','GDPR blah blah blah','Steve Smith')
risk_repository.save(risk4)
risk5 = Risk('Identity & Access Management risk','IAM blah blah blah','Steve Smith')
risk_repository.save(risk5)
risk6 = Risk('Identity & Access Management risk','IAM blah blah blah','Steve Smith')
risk_repository.save(risk6)
risk7 = Risk('Business Continuity risk','Business Continuity blah blah blah','Steve Smith')
risk_repository.save(risk7)

### Control(title,description,owner) ###
control1 = Control("Create a web app",consultant1,client1,10,"2021-01-01","2021-01-21",5000)
control_repository.save(control1)


pdb.set_trace()