from db.run_sql import run_sql

from models.manufacturer import manufacturer


def save(manufacturer):
    sql = "INSERT INTO manufacturers (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.first_name, manufacturer.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturer =[]

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer(row['first_name'], 
        row['last_name'], row['id'])
        manufacturers.append(manufacturer)
        return manufacturer