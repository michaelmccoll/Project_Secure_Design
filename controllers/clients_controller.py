from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import consultant_repository, client_repository, assignment_repository
from models.client import Client

clients_blueprint = Blueprint("clients",__name__)

@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    return render_template("clients/index.html", all_clients=clients)

@clients_blueprint.route("/clients/new")
def new_client():
    return render_template("clients/new.html")

@clients_blueprint.route("/clients", methods=['POST'])
def create_client():
    name = request.form["name"]
    type_of_business = request.form["type_of_business"]
    contact_details = request.form["contact_details"]
    new_client = Client(name,type_of_business,contact_details)
    client_repository.save(new_client)
    return redirect("/clients")

@clients_blueprint.route("/clients/<id>")
def show_client(id):
    client = client_repository.select(id)
    consultants = consultant_repository.consultants(client)
    assignments = assignment_repository.assignments(client)
    return render_template("clients/show.html",client=client,consultants=consultants,assignments=assignments)

@clients_blueprint.route("/clients/<id>/edit", methods=['GET'])
def edit_client(id):
    client = client_repository.select(id)
    return render_template("/clients/edit.html", client=client)

@clients_blueprint.route("/clients/<id>", methods=['POST'])
def update_client(id):
    name = request.form["name"]
    type_of_business = request.form["type_of_business"]
    contact_details = request.form["contact_details"]
    client = Client(name,type_of_business,contact_details,id)
    client_repository.update(client)
    return redirect("/clients")

@clients_blueprint.route("/clients/<id>/delete", methods=['POST'])
def delete_client(id):
    client_repository.delete(id)
    return redirect ("/clients")