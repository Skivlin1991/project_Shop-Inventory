from models.stock.py import stock
from models.manufacturer.py import manufacturer
import manufacturer_repository 

def select_all():
    stock = []

    sql = "SELECT * FROM stock"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        stock = Stock (row['description'], )