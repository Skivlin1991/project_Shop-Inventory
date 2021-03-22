from app.models.manufacturer import Manufacturer


class Stock:
    
    def __init__(self, name, description , cost, price ,id =None):
            self.name = name
            self.description= description
            self. manufacturer= Manufacturer
            self.id=id
            self.cost = cost
            self.price = price

    def mark_sold(self):
        self.completed = True