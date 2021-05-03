import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


csvfile = "ST43_3092_202103.csv"
with open(csvfile, 'r') as fp:
     reader = csv.reader(fp)
     for row in reader:
          print(row)

