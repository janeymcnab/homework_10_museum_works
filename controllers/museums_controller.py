from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
import repositories.museum_repository as museum_repository

museums_blueprint = Blueprint("museums", __name__)

# INDEX
# GET '/museums

@museums_blueprint.route('/museums')
def museums():
    museums = museum_repository.select_all()
    return render_template('museums/index.html', museums = museums)

# NEW
# GET '/museums/new'

@museums_blueprint.route("/museums/new", methods=['GET']) 
def new_museum():
     return render_template("museums/new.html")

# CREATE
# POST '/museums'
@museums_blueprint.route("/museums",  methods=['POST'])
def create_museum():
    name = request.form['name']
    address = request.form['address']
    museum = Museum(name, address)
    museum_repository.save(museum)
    return redirect('/museums')

# SHOW
# GET '/museums/<id>'

@museums_blueprint.route("/museums/<id>", methods=['GET'])
def show_museum(id):
    museum = museum_repository.select(id)
    return render_template('museums/show.html', museum = museum)

# EDIT
# GET '/museums/<id>/edit'

# UPDATE
# PUT '/museums/<id>'

# DELETE
# DELETE '/museums/<id>'

