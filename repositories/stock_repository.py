from models.manufacturer import Manufacturer
from models.stock import Stock 
from db import run_sql
# from apps.models.manufacturer import Manufacturer
# from apps.repositories.stock_repository import stock_repository


def save(stock):
    sql = "INSERT INTO stock(name , description , manufacturer ,cost, price ,id ) VALUES (%s, %s, %s, %s, %s,) RETURNING *"
    values = [stock.name, stock.description, stock.manufacturer, stock.cost, stock.price, stock.id ]
    results = run_sql(sql, values)
    id = results[0]['id']
    stock.id = id
    return stock

def select_all():
    stock =[]

    sql = "SELECT * FROM stock"
    results = run_sql(sql)

    for row in results:
        stock = stock(row['name'], 
        row['description'], row['manufacturer'], row['cost'], row['price'], row['id'])
        stock.append(stock)
        return stock

def select(id):
    stock = None
    sql = "SELECT * FROM stock WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
       stock = stock(result['first_name'], result['last_name'], result['id'])
    return manufacturer
        
def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturer WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturer SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [manufacturer.first_name, manufacturer.last_name, manufacturer.id]
    run_sql(sql, values)

def stock(manufacturer):
    stock = []

    sql = "SELECT * FROM stock WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)
    for row in results:
        stock = stock(row['name'], row['description'], row['manufacturer'], row['cost'], row['price'], row ['id'] )
        stock.append(stock)
    return stock

    