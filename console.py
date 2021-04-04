import pdb

from models.project import Project
from models.triage import Triage
from models.categories import Category
from models.risk import Risk
from models.control import Control

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository
import repositories.category_repository as category_repository

project_repository.delete_all()
triage_repository.delete_all()
risk_repository.delete_all()
control_repository.delete_all()

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

### Categories (category) ###
category1 = Category('Identity & Access Management')
category_repository.save(category1)
category2 = Category('Infrastructure')
category_repository.save(category2)
category3 = Category('Supplier')
category_repository.save(category3)
category4 = Category('GDPR')
category_repository.save(category4)
category5 = Category('Business Continuity')
category_repository.save(category5)
category6 = Category('Confidentiality')
category_repository.save(category6)
category7 = Category('Integrity')
category_repository.save(category7)
category8 = Category('Availability')
category_repository.save(category8)

### Triage(question,project,category,date) ### This may not be the best place to put date, as it repeats
triage1 = Triage('Is the project implementing or changing any Identity & Access Managment methods?',project1,category1,'2021-03-01')
triage_repository.save(triage1)
triage2 = Triage('Is the project implementing or changing any Infrastructure',project1,category2,'2021-03-01')
triage_repository.save(triage2)
triage3 = Triage('Is the project implementing or changing any Supplier Relationships?',project1,category3,'2021-03-01')
triage_repository.save(triage3)
triage4 = Triage('Is the project implementing or changing any Personally Identifiable Information?',project1,category4,'2021-03-01')
triage_repository.save(triage4)
triage5 = Triage('What is the Confidentiality rating of information involved?',project1,category6,'2021-03-01')
triage_repository.save(triage5)
triage6 = Triage('What is the Integrity rating of information involved?',project1,category7,'2021-03-01')
triage_repository.save(triage6)
triage7 = Triage('What is the Availability rating of information involved?',project1,category8,'2021-03-01')
triage_repository.save(triage7)
triage8 = Triage('What is the highest Business Continuity rating of the processes involved?',project1,category5,'2021-03-01')
triage_repository.save(triage8)
# triage7 not linked to a risk yet, could maybe be included in risk7

### Risk(title,description,owner,triage,category) ###
risk1 = Risk('Identity & Access Management risk','IAM blah blah blah','Steve Smith',triage1,category1)
risk_repository.save(risk1)
risk2 = Risk('Infrastructure risk','Infrastructure blah blah blah','Bob Hall',triage2,category2)
risk_repository.save(risk2)
risk3 = Risk('Supplier risk','Supplier blah blah blah','Peter Edinburgh',triage3,category3)
risk_repository.save(risk3)
risk4 = Risk('GDPR risk','GDPR blah blah blah','Jean Scotland',triage4,category4)
risk_repository.save(risk4)
risk5 = Risk('Unauthorised Data Access risk','Unauthorised Access blah blah blah','Steve Smith',triage5,category6)
risk_repository.save(risk5)
risk6 = Risk('Data Quality risk','Data Quality blah blah blah','Bob Hall',triage6,category7)
risk_repository.save(risk6)
risk7 = Risk('Business Continuity risk','Business Continuity blah blah blah','Tony Ford',triage8,category5)
risk_repository.save(risk7)

### Control(title,description,owner,risk,category) ###
control1 = Control('Access Control','Access control details for IAM Risk...','Steve Smith',risk1,category1)
control_repository.save(control1)
control2 = Control('Identity Control','Identity control details for IAM Risk...','Steve Smith',risk1,category1)
control_repository.save(control2)
control3 = Control('Authentication Control','Authentication control details for IAM Risk...','Steve Smith',risk1,category1)
control_repository.save(control3)
control4 = Control('Server Control','Server control details for Infrastructure Risk...','Bob Hall',risk2,category2)
control_repository.save(control4)
control5 = Control('Cloud Control','Cloud control details for Infrastructure Risk...','Bob Hall',risk2,category2)
control_repository.save(control5)
control6 = Control('Due Diligence Control','Due Diligence control details for Supplier Risk...','Peter Edinburgh',risk3,category3)
control_repository.save(control6)
control7 = Control('Supplier Review Control','Supplier Review control details for Supplier Risk...','Peter Edinburgh',risk3,category3)
control_repository.save(control7)
control8 = Control('Data Privacy Control','Data Privacy control details for GDPR Risk...','Jean Scotland',risk4,category4)
control_repository.save(control8)
control9 = Control('Info Classification Control','Info Classification control details for Confidentiality Risk...','Steve Smith',risk5,category6)
control_repository.save(control9)
control10 = Control('Data Validation Control','Data Validation control details for Data Quality Risk...','Bob Hall',risk6,category7)
control_repository.save(control10)
control11 = Control('Data Cleansing Control','Data Cleansing control details for Data Quality Risk...','Bob Hall',risk6,category7)
control_repository.save(control11)
control12 = Control('Continuity Plan Control','Continuity Plan control details for Business Continuity Risk...','Tony Ford',risk7,category5)
control_repository.save(control12)
control13 = Control('IT Disaster Recovery Control','IT Disaster Recovery control details for Business Continuity Risk...','Tony Ford',risk7,category5)
control_repository.save(control13)

pdb.set_trace()