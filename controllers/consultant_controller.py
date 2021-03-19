from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository
from models.consultant import Consultant

consultants_blueprint = Blueprint("consultants",__name__)

# @consultants_blueprint.route('/consultants')