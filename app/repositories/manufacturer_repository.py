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

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
       manufacturer = manufacturer(result['first_name'], result['last_name'], result['id'])
    return manufacturer
        
def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturer WHERE id = %s"
    values = [id]
    run_sql(sql, vlaues)

def update(manufacturer):
    sql = ""
