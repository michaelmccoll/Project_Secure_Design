import pdb

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.control import Control

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository

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

### Triage(project,iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date,id)
triage1 = Triage(project1,'Yes','No','Yes','Yes','Confidential','Medium','High','Critical','2021-03-01')
triage_repository.save(triage1)
triage2 = Triage(project4,'Yes','Yes','Yes','Yes','Highly Confidential','High','Low','Important','2021-05-01')
triage_repository.save(triage2)

### Risk(title,description,owner,triage) ###
risk1 = Risk('Identity & Access Management risk','IAM blah blah blah','Steve Smith',triage1)
risk_repository.save(risk1)
risk2 = Risk('Infrastructure risk','Infrastructure blah blah blah','Bob Hall',triage1)
risk_repository.save(risk2)
risk3 = Risk('Supplier risk','Supplier blah blah blah','Peter Edinburgh',triage1)
risk_repository.save(risk3)
risk4 = Risk('GDPR risk','GDPR blah blah blah','Jean Scotland',triage1)
risk_repository.save(risk4)
risk5 = Risk('Unauthorised Data Access risk','Unauthorised Access blah blah blah','Steve Smith',triage1)
risk_repository.save(risk5)
risk6 = Risk('Data Quality risk','Data Quality blah blah blah','Bob Hall',triage1)
risk_repository.save(risk6)
risk7 = Risk('Business Continuity risk','Business Continuity blah blah blah','Tony Ford',triage1)
risk_repository.save(risk7)

### Control(title,description,owner,risk) ###
control1 = Control('Access Control','Access control details for IAM Risk...','Steve Smith',risk1)
control_repository.save(control1)
control2 = Control('Identity Control','Identity control details for IAM Risk...','Steve Smith',risk1)
control_repository.save(control2)
control3 = Control('Authentication Control','Authentication control details for IAM Risk...','Steve Smith',risk1)
control_repository.save(control3)
control4 = Control('Server Control','Server control details for Infrastructure Risk...','Bob Hall',risk2)
control_repository.save(control4)
control5 = Control('Cloud Control','Cloud control details for Infrastructure Risk...','Bob Hall',risk2)
control_repository.save(control5)
control6 = Control('Due Diligence Control','Due Diligence control details for Supplier Risk...','Peter Edinburgh',risk3)
control_repository.save(control6)
control7 = Control('Supplier Review Control','Supplier Review control details for Supplier Risk...','Peter Edinburgh',risk3)
control_repository.save(control7)
control8 = Control('Data Privacy Control','Data Privacy control details for GDPR Risk...','Jean Scotland',risk4)
control_repository.save(control8)
control9 = Control('Info Classification Control','Info Classification control details for Confidentiality Risk...','Steve Smith',risk5)
control_repository.save(control9)
control10 = Control('Data Validation Control','Data Validation control details for Data Quality Risk...','Bob Hall',risk6)
control_repository.save(control10)
control11 = Control('Data Cleansing Control','Data Cleansing control details for Data Quality Risk...','Bob Hall',risk6)
control_repository.save(control11)
control12 = Control('Continuity Plan Control','Continuity Plan control details for Business Continuity Risk...','Tony Ford',risk7)
control_repository.save(control12)
control13 = Control('IT Disaster Recovery Control','IT Disaster Recovery control details for Business Continuity Risk...','Tony Ford',risk7)
control_repository.save(control13)

pdb.set_trace()