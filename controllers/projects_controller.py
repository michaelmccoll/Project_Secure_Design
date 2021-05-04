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
    return render_template("/projects/new.html")

@projects_blueprint.route("/projects", methods=['POST'])
def create_project():
    title = request.form["title"]
    sponsor = request.form["sponsor"]
    project_manager = request.form["project_manager"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    status = request.form["status"]
    new_project = Project(title,sponsor,project_manager,start_date,end_date,status)
    project_repository.save(new_project)
    return redirect("/projects")

@projects_blueprint.route("/projects/<id>")
def show_project(id):
    project = project_repository.select(id)
    # need to feed 'project_id' (19) into next line, that then returns triage 'id' (8)
    # OR refactor to include triage Id in the project table
    triage = triage_repository.select(id)
    # risks = risk_repository.risks(project)
    # controls = control_repository.controls(project)
    return render_template("/projects/show.html",project=project,triage=triage)

@projects_blueprint.route("/projects/<id>/edit", methods=['GET'])
def edit_project(id):
    project = project_repository.select(id)
    return render_template("/projects/edit.html", project=project)

@projects_blueprint.route("/projects/<id>", methods=['POST'])
def update_project(id):
    title = request.form["title"]
    sponsor = request.form["sponsor"]
    project_manager = request.form["project_manager"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    status = request.form["status"]
    project = Project(title,sponsor,project_manager,start_date,end_date,status,id)
    project_repository.update(project)
    return redirect("/projects")

@projects_blueprint.route("/projects/<id>/delete", methods=['POST'])
def delete_project(id):
    project_repository.delete(id)
    return redirect ("/projects")