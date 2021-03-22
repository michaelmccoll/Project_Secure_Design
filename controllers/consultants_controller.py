from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository, assignment_repository
from models.consultant import Consultant

consultants_blueprint = Blueprint("consultants",__name__)

@consultants_blueprint.route("/consultants")
def consultants():
    consultants = consultant_repository.select_all()
    return render_template("consultants/index.html", all_consultants=consultants)

@consultants_blueprint.route("/consultants/new")
def new_consultant():
    return render_template("consultants/new.html")

@consultants_blueprint.route("/consultants", methods=['POST'])
def create_consultant():
    name = request.form["name"]
    role = request.form["role"]
    summary = request.form["summary"]
    day_rate = request.form["day_rate"]
    new_consultant = Consultant(name,role,summary,day_rate)
    consultant_repository.save(new_consultant)
    return redirect("/consultants")

@consultants_blueprint.route("/consultants/<id>")
def show_consultant(id):
    consultant = consultant_repository.select(id)
    found_clients = client_repository.clients(consultant) #needs created
    found_assignments = assignment_repository.assignments(consultant) #needs created
    return render_template("consultants/show.html",consultant=consultant,clients=found_clients,assignments=found_assignments)
