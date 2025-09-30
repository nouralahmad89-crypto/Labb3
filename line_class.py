import matplotlib.pyplot as plt
import numpy as np



# a)  läsa in filen unlabelled_data.csv och plotta innehållet
d1 , d2 = [] ,[]
try:
    with open("unlabelled_data.csv", "r") as data:
        for line in data:
            x_val, y_val = map(float, line.strip().split(","))
            d1.append(x_val)
            d2.append(y_val)
except FileNotFoundError:            
    raise FileNotFoundError(" file Not Found , Make Sure Path is correct")
x=np.array(d1)
y=np.array(d2)
plt.figure(figsize=(7,5) , dpi = 100)
plt.scatter(d1, d2, label="Data points" , c="red" , marker="*")
plt.title("Scatter plot of data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()