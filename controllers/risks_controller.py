from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import project_repository, triage_repository, risk_repository, control_repository, category_repository
from models.risk import Risk

risks_blueprint = Blueprint("risks",__name__)

@risks_blueprint.route('/risks')
def risks():
    risks = risk_repository.select_all()
    return render_template("/risks/index.html", all_risks=risks)

@risks_blueprint.route("/risks/new")
def new_risk():
    projects = project_repository.select_all()
    triages = triage_repository.select_all()
    return render_template("risks/new.html", all_projects=projects, all_triages=triages)

@risks_blueprint.route("/risks", methods=['POST'])
def create_risk():
    description = request.form["description"]
    project_id = request.form["project_id"]
    project = project_repository.select(project_id)
    triage_id = request.form["triage_id"]
    triage = triage_repository.select(triage_id)
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    days_required = request.form["days_required"]
    calculate_costs = risk.calculate_costs(project.day_rate,days_required)
    new_risk = risk(description,project,triage,days_required,start_date,end_date, calculate_costs)
    risk_repository.save(new_risk)
    return redirect("/risks")

@risks_blueprint.route("/risks/<id>")
def show_risk(id):
    risk = risk_repository.select(id)
    triages = triage_repository.triages(risk)
    projects = project_repository.projects(risk)
    return render_template("/risks/show.html",risk=risk,triages=triages,projects=projects)

@risks_blueprint.route("/risks/<id>", methods=['POST'])
def update_risk(id):
    description = request.form["description"]
    project_id = request.form["project_id"]
    project = project_repository.select(project_id)
    triage_id = request.form["triage_id"]
    triage = triage_repository.select(triage_id)
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    days_required = request.form["days_required"]
    calculate_costs = risk.calculate_costs(project.day_rate,days_required)
    risk = risk(description,project,triage,days_required,start_date,end_date,calculate_costs,id)
    risk_repository.update(risk)
    return redirect("/risks")

@risks_blueprint.route("/risks/<id>/edit", methods=['GET'])
def edit_risk(id):
    risk = risk_repository.select(id)
    triages = triage_repository.select_all()
    projects = project_repository.select_all()
    return render_template("/risks/edit.html", risk=risk,triages=triages,projects=projects)

@risks_blueprint.route("/risks/<id>/delete", methods=['POST'])
def delete_risk(id):
    risk_repository.delete(id)
    return redirect ("/risks")