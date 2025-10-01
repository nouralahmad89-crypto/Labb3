import matplotlib.pyplot as plt
import numpy as np



# a)  läsa in filen unlabelled_data.csv och plotta innehållet
d1, d2 = [] , []
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
plt.scatter(d1, d2, label="Data points" , c="red" , marker="*")
plt.title("Scatter plot of data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Beräkna linjen som delar punkterna
x_val= np.mean(x)
y_val= np.mean(y)
# när x=0 => m=y , nu har vi två punlter ( x_val, y_val ), (0,m)
k= -1
# räkan m värde k= x_val-0 / y_val-m => m= x_val+y_val
m= x_val+ y_val
y= -1*x+ m
plt.scatter(d1, d2, label="Data points" , c="red" , marker="*")
plt.plot(x, y,)
plt.title("Scatter plot of data med linje")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
plt.show()

