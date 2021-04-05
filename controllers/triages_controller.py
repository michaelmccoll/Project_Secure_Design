from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import project_repository, triage_repository, risk_repository, control_repository
from models.triage import Triage

triages_blueprint = Blueprint("triages",__name__)

@triages_blueprint.route("/triages")
def triages():
    triages = triage_repository.select_all()
    return render_template("triages/index.html", all_triages=triages)

@triages_blueprint.route("/triages/new")
def new_triage():
    return render_template("triages/new.html")

@triages_blueprint.route("/triages", methods=['POST'])
def create_triage():
    name = request.form["name"]
    type_of_business = request.form["type_of_business"]
    contact_details = request.form["contact_details"]
    new_triage = Triage(name,type_of_business,contact_details)
    triage_repository.save(new_triage)
    return redirect("/triages")

@triages_blueprint.route("/triages/<id>")
def show_triage(id):
    triage = triage_repository.select(id)
    projects = project_repository.projects(triage)
    risks = risk_repository.risks(triage)
    return render_template("triages/show.html",triage=triage,projects=projects,risks=risks)

@triages_blueprint.route("/triages/<id>/edit", methods=['GET'])
def edit_triage(id):
    triage = triage_repository.select(id)
    return render_template("/triages/edit.html", triage=triage)

@triages_blueprint.route("/triages/<id>", methods=['POST'])
def update_triage(id):
    name = request.form["name"]
    type_of_business = request.form["type_of_business"]
    contact_details = request.form["contact_details"]
    triage = Triage(name,type_of_business,contact_details,id)
    triage_repository.update(triage)
    return redirect("/triages")

@triages_blueprint.route("/triages/<id>/delete", methods=['POST'])
def delete_triage(id):
    triage_repository.delete(id)
    return redirect ("/triages")