from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import project_repository, triage_repository, risk_repository, control_repository
from models.project import Project

projects_blueprint = Blueprint("projects",__name__)

@projects_blueprint.route("/projects")
def projects():
    projects = project_repository.select_all()
    return render_template("projects/index.html", all_projects=projects)

@projects_blueprint.route("/projects/new")
def new_project():
    return render_template("projects/new.html")

@projects_blueprint.route("/projects", methods=['POST'])
def create_project():
    name = request.form["name"]
    role = request.form["role"]
    summary = request.form["summary"]
    day_rate = request.form["day_rate"]
    new_project = Project(name,role,summary,day_rate)
    project_repository.save(new_project)
    return redirect("/projects")

@projects_blueprint.route("/projects/<id>")
def show_project(id):
    project = project_repository.select(id)
    triage = triage_repository.triage(project)
    risks = risk_repository.risks(project)
    controls = control_repository.controls(project)
    return render_template("projects/show.html",project=project,triage=triage,risks=risks,controls=controls)

@projects_blueprint.route("/projects/<id>/edit", methods=['GET'])
def edit_project(id):
    project = project_repository.select(id)
    return render_template("/projects/edit.html", project=project)

@projects_blueprint.route("/projects/<id>", methods=['POST'])
def update_project(id):
    name = request.form["name"]
    role = request.form["role"]
    summary = request.form["summary"]
    day_rate = request.form["day_rate"]
    project = Project(name,role,summary,day_rate,id)
    project_repository.update(project)
    return redirect("/projects")

@projects_blueprint.route("/projects/<id>/delete", methods=['POST'])
def delete_project(id):
    project_repository.delete(id)
    return redirect ("/projects")