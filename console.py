from flask import flask
from models.manufacturer import manufacturer
from modeels.stock import stock

import repositories.manufacturer_repositories as manufacturer_repository
import repositories.stock_repositories as stock_repository

manufacturer_repository.delete_all()
stock_repository.delete_all()

manufacturer1 = manufacturer("Onyxhand","Dustcounter")
manufacturer_repository.save(manufacturer1)
manufacturer2 = manufacturer("Galan","Thetris")
manufacturer_repository.save(manufacturer2)
manufacturer3 = manufacturer("Kormdek","Bronzebrowser")

manufacturer_repository.select_all()

pdb.set_trace()