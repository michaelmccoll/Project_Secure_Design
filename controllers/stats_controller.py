from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import project_repository, triage_repository, risk_repository, control_repository

stats_blueprint = Blueprint("stats",__name__)

@stats_blueprint.route("/stats")
def stats():
    projects = project_repository.select_all()
    triages = triage_repository.select_all()
    risks = risk_repository.select_all()
    total_income = risk_repository.total_income()
    total_days_required = risk_repository.total_days_required()
    total_triage_spend = triage_repository.total_triage_spend()
    total_project_income = project_repository.total_project_income()
    return render_template("stats/index.html", projects=projects,triages=triages,risks=risks,total_income=total_income,total_days_required=total_days_required,total_triage_spend=total_triage_spend,total_project_income=total_project_income)

