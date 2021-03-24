from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository, assignment_repository
from models.consultant import Consultant

admins_blueprint = Blueprint("admins",__name__)

@admins_blueprint.route("/admins")
def admins():
    consultants = consultant_repository.select_all()
    clients = client_repository.select_all()
    assignments = assignment_repository.select_all()
    return render_template("admins/index.html", consultants=consultants,clients=clients,assignments=assignments)