from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.stock import Stock 

import repositories.manufacturer_repository as manufacturer_repository

# from apps.models.manufacturer import Manufacturer
# from apps.repositories.stock_repository import stock_repository


def save(stock):
    sql = "INSERT INTO stock (name, description, manufacturer_id, cost, price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [stock.name, stock.description, stock.manufacturer.id, stock.cost, stock.price ]
    results = run_sql(sql, values)
    id = results[0]['id']
    stock.id = id
    return stock

def select_all():
    stock = []

    sql = "SELECT * FROM stock"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        new_stock = Stock(row['name'], row['description'], manufacturer, row['cost'], row['price'], row['id'])
        stock.append(new_stock)
    return stock
        

def select(id):
    stock = None
    sql = "SELECT * FROM stock WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
       manufacturer = manufacturer_repository.select(result['manufacturer_id']) 
       stock = Stock(result['name'], result['description'], manufacturer, result['cost'] ,result['price'] , result['id'])
    return stock
        
def delete_all():
    sql = "DELETE FROM stock"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM stock WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(stock):
    sql = "UPDATE stock SET (self, name, description , manufacturer ,cost, price ,id)"
    values = [stock.name, stock.description , stock.manufacturer ,stock.cost, stock.price ,stock.id]
    run_sql(sql, values)
    