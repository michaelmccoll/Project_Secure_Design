from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository, assignment_repository
from models.assignment import Assignment

assignments_blueprint = Blueprint("assignments",__name__)

@assignments_blueprint.route('/assignments')
def assignments():
    assignments = assignment_repository.select_all()
    return render_template("assignments/index.html", all_assignments=assignments)