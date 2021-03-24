from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository, assignment_repository

stats_blueprint = Blueprint("stats",__name__)

@stats_blueprint.route("/stats")
def stats():
    consultants = consultant_repository.select_all()
    clients = client_repository.select_all()
    assignments = assignment_repository.select_all()
    total_income = assignment_repository.total_income()
    total_days_required = assignment_repository.total_days_required()
    total_client_spend = client_repository.total_client_spend()
    total_consultant_income = consultant_repository.total_consultant_income()
    return render_template("stats/index.html", consultants=consultants,clients=clients,assignments=assignments,total_income=total_income,total_days_required=total_days_required,total_client_spend=total_client_spend,total_consultant_income=total_consultant_income)

