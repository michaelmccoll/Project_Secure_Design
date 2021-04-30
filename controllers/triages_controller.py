from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import project_repository, triage_repository, risk_repository, control_repository
from models.triage import Triage

triages_blueprint = Blueprint("triages",__name__)

@triages_blueprint.route("/triages")
def triages():
    triages = triage_repository.select_all()
    return render_template("/triages/index.html", all_triages=triages)

@triages_blueprint.route("/triages/new")
def new_triage():
    return render_template("triages/new.html")

@triages_blueprint.route("/triages", methods=['POST'])
def create_triage():
    project = project_repository.select(project_id)
    iam = request.form["iam"]
    infrastructure = request.form["infrastructure"]
    supplier = request.form["supplier"]
    privacy = request.form["privacy"]
    confidentiality = request.form["confidentiality"]
    integrity = request.form["integrity"]
    availability = request.form["availability"]
    continuity = request.form["continuity"]
    date = request.form["date"]
    new_triage = Triage(project,iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date)
    triage_repository.save(new_triage)
    return redirect("/triages")

@triages_blueprint.route("/triages/<id>")
def show_triage(id):
    triage = triage_repository.select(id)
    projects = project_repository.projects(triage)
    risks = risk_repository.risks(triage)
    return render_template("/triages/show.html",triage=triage,projects=projects,risks=risks)

@triages_blueprint.route("/triages/<id>/edit", methods=['GET'])
def edit_triage(id):
    triage = triage_repository.select(id)
    return render_template("/triages/edit.html", triage=triage)

@triages_blueprint.route("/triages/<id>", methods=['POST'])
def update_triage(id):
    project = request.form["project"]
    iam = request.form["iam"]
    infrastructure = request.form["infrastructure"]
    supplier = request.form["supplier"]
    privacy = request.form["privacy"]
    confidentiality = request.form["confidentiality"]
    integrity = request.form["integrity"]
    availability = request.form["availability"]
    continuity = request.form["continuity"]
    date = request.form["date"]
    triage = Triage(project,iam,infrastructure,supplier,privacy,confidentiality,integrity,availability,continuity,date,id)
    triage_repository.update(triage)
    return redirect("/triages")

@triages_blueprint.route("/triages/<id>/delete", methods=['POST'])
def delete_triage(id):
    triage_repository.delete(id)
    return redirect ("/triages")