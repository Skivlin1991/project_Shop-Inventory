from typing import ValuesView


class Manufacturer:
    
    def __init__(self, first_name, last_name, id =None):
        self.first_name=first_name
        self.last_name=last_name
        self.id = id

    def save(stock):
        sql = "INSERT INTO stock (name, description, cost, price ,id)
        ValuesView (%s,%s,%s,%s,%s) RETURNING *"
        values = [stock.name, stock.description, stock.cost, stock.price, stock.id]
        results = run_sql(sql, values)
        id = results[0]['id']
        stock.id = id 
        return stock