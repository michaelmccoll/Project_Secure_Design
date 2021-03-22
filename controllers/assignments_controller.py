from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository, assignment_repository
from models.assignment import Assignment

assignments_blueprint = Blueprint("assignments",__name__)

@assignments_blueprint.route('/assignments')
def assignments():
    assignments = assignment_repository.select_all()
    return render_template("assignments/index.html", all_assignments=assignments)

@assignments_blueprint.route("/assignments/new")
def new_assignment():
    consultants = consultant_repository.select_all()
    clients = client_repository.select_all()
    return render_template("assignments/new.html", all_consultants=consultants, all_clients=clients)

@assignments_blueprint.route("/assignments", methods=['POST'])
def create_assignment():
    description = request.form["description"]
    consultant_id = request.form["consultant_id"]
    consultant = consultant_repository.select(consultant_id)
    client_id = request.form["client_id"]
    client = client_repository.select(client_id)
    days_required = request.form["days_required"]
    new_assignment = Assignment(description,consultant,client,days_required)
    assignment_repository.save(new_assignment)
    return redirect("/assignments")