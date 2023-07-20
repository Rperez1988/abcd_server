
import csv

from models import stock

def run():
    fhand = open("../AACG.csv")
    reader = csv.reader(fhand)

