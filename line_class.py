import matplotlib.pyplot as plt
import numpy as np
import csv


# a)  ====läsa in filen unlabelled_data.csv och plotta innehållet====
path= "unlabelled_data.csv"

def get_data(path):
    d1, d2 = [] , []
    try:
        with open(path, "r" , newline="") as data:
           reader= csv.reader(data) # skaper en csv läsare
           for row in reader:
               x_val, y_val = map(float, row[:2])
               d1.append(x_val)
               d2.append(y_val)
    except FileNotFoundError:            
        raise FileNotFoundError(" file Not Found , Make Sure Path is correct")
    return d1, d2

d1,d2 = get_data(path) # anropa funktion

# ====plotta data punkter====
def draw_point(x,y):
    plt.figure(figsize=(7,5))
    plt.scatter(d1, d2, label="Data points" , color="red" , marker="*")
    plt.title("Scatter plot of data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
draw_point(d1 , d2)    

