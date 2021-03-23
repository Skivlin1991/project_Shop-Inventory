import pdb
from flask import Flask
from models.manufacturer import Manufacturer
from models.stock import Stock

import repositories.manufacturer_repository as manufacturer_repository
import repositories.stock_repository as stock_repository

manufacturer_repository.delete_all()

stock_repository.delete_all()

manufacturer1 = Manufacturer("Onyxhand","Dustcounter")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("Galan","Thetris")
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer("Kormdek","Bronzebrowser")

#  name, description , manufacturer ,cost, price 
stock_1 = ("Bag of holding", "Wondrous Item", "100 Gold","175 Gold", manufacturer1)
stock_repository.save(stock_1)
stock_2 = ("Ivory Goat", "Wonderous Item", "300 Gold","424 Gold", manufacturer1)
stock_repository.save(stock_2)

stock_3 = ("Necklace Of Fireballs", "Wonderous Item", "400 Gold","510 Gold", manufacturer2)
stock_repository.save(stock_3)
stock_4 = ("Ring Of Feather Falling", "Wonderous Item", "2000 Gold","3250 Gold", manufacturer2)
stock_repository.save(stock_4)

stock_5 = ("Flame Tongue", "Weapon(greatsword)", "4000 Gold","5550 Gold", manufacturer3)
stock_repository.save(stock_5)
stock_6 = ("Vorpal Sword", "Weapon(legendary)", "20,000 Gold","45,000 Gold" ,manufacturer3)
stock_repository.save(stock_6)

manufacturer_repository.select_all()

pdb.set_trace()
