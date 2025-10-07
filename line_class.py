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
plt.figure(figsize=(7,5))
plt.scatter(d1, d2, label="Data points" , color="red" , marker="*")
plt.title("Scatter plot of data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
# convert till numpy-array
x= np.array(d1)
y=np.array(d2)
"""Beräkna linjen som delar punkterna
 så jämnt som möjligt"""
# Beräknar medelvärdet av x och y för att hitta en punkt nära datats centrala punkt
x_val= np.mean(x)
y_val= np.mean(y)
# när x=0 => m=y , nu har vi två punkter ( x_val, y_val ), (0,m)
k= -1
# räkan m värde:  k = x_val- 0 / y_val- m => m = x_val + y_val
m= x_val+ y_val
x_line = np.linspace(min(x), max(x), 100)
y_line = -1*x_line+ m
print(f"Ekvation: y={k}x+{m:.2f}")
plt.figure( figsize=(7,5))
plt.scatter(d1, d2, label="Data points" , c="red" , marker="*")
plt.plot(x_line, y_line, label="Y=kx+m" ,color= "blue")
plt.title("Scatter plot of data med linje")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
