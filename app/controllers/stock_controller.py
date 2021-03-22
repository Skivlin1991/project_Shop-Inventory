from flask from app.models.manufacturer import Manufacturer
import Flask, render_template, request, redirect
from flask import Blueprint
from models.stock import stock
import repositories.stock_repository as stock_repository
import repositories.manufacturer_repository as manufacturer_repository

stock_blueprint = Blueprint("stock", __name__)

@stock_blueprint.route("/stock")
def stock():
    stock = stock_repository.select_all() # NEW
    return render_template("stock/index.html", all_stock = stock)
    
# NEW
# GET '/stock/new'
@stock_blueprint.route("/stock/new", methods=['GET'])
def new_stock():
    manufacturer = manufacturer_repository.select_all()
    return render_template("stock/new.html", all_manufacturer = manufacturers)

# CREATE
# POST '/stock'
@stock_blueprint.route("/stocks",  methods=['POST'])
def create_stock():
    name = request.form['name']
    description = request.form['description']
    manufacturer = request.form['manufacturer']
    price = request.form['price']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    stock = stock(name, description , price ,id)
    stock_repository.save(stock)
    return redirect('/stock')

# SHOW
# GET '/stock/<id>'
@stock_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)

# EDIT
# GET '/stock/<id>/edit'
@stock_blueprint.route("/stock/<id>/edit", methods=['GET'])
def edit_stock(id):
    stock = stock_repository.select(id)
    manufacturer = manufacturer_repository.select_all()
    return render_template('stock/edit.html', stock = stock, all_manufacturer = manufacturer)

# UPDATE
# PUT '/stock/<id>'
@stock_blueprint.route("/stock/<id>", methods=['POST'])
def update_stock(id):
    name  = request.form['title']
    description = request.form['description']
    price = requset.form['price']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    stock= stock(name, description ,price ,id )
    print(stock.manufacturer.full_name())
    stock_repository.update(stock)
    return redirect('/stock')

# DELETE
# DELETE '/books/<id>'
@stock_blueprint.route("/stock/<id>/delete", methods=['POST'])
def delete_stock(id):
    stock_repository.delete(id)
    return redirect('/stock')