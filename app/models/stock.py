class stock:
    def __init__(self, name, description , cost, price ,id =None):
            self.name = name
            self.description=description
            self.id=id
            self.cost = cost
            self.price = price

    def mark_sold(self):
        self.completed = True