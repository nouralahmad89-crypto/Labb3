import numpy as np
import matplotlib.pyplot as plt
import csv
import line_class as ln

# c) en funktion för att classifiey punkter position 
def point_position(x_point, y_point, k, m):
    """
    Bestämmer om en punkt ligger ovanför (höger) eller under (vänster) 
    om linjen y = kx + m 
    Returnerar:
        0 om punkten ligger under/eller vänster om linjen
        1 om punkten ligger ovanför/eller höger om linjen
    """
    line_y = k * x_point + m   # Beräkna y-värdet på linjen vid x_point
    if y_point > line_y:
      return 1  #höger om linjen
    else:
      return 0  # vänster om linjen
    
 # d) klassifiera alla punkterna i unlabelled_data.csv filen.   
points= list(zip(ln.d1,ln.d2)) # Skapar en lista av tupler med punkter (x, y)
labels=[] # en list för spara labels
for p in points:
    label= point_position(p[0],p[1], ln.k , ln.m)
    labels.append(label) 

# e) skaffa labelled.csv fil

with open("labelled_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([" x Values ", " y Values ", "label"])  # rubriker
    for p in points:
        label = point_position(p[0], p[1], ln.k, ln.m)
        writer.writerow([p[0], p[1], label])
print("Filen 'labelled_data.csv' har skapats med etiketter (0/1)")

# f) Ett fönster med en graf där punkterna, deras klass och din linje 
x_values, y_values, labels = [] , [], []
with open( "labelled_data.csv", "r", newline="") as lb_data:
   reader= csv.reader(lb_data)
   next(reader) # hoppa över header
   for line in reader:
        x_values.append(float(line[0]))
        y_values.append(float(line[1]))
        labels.append(int(line[2]))
x_values= np.array(x_values)
y_values= np.array(y_values)
labels= np.array(labels)        
upper_indx= np.where(labels==1) # hämta indecies för alla höger punkter
lower_indx= np.where(labels==0) # hämta indecies för all vänster punkter
plt.figure( figsize=(7,5))
plt.scatter(x_values[upper_indx], y_values[upper_indx], label="Data points above line" , color="red" , marker="*")
plt.scatter(x_values[lower_indx], y_values[lower_indx], label="Data points lower line" , color="green" , marker="*")
plt.plot(ln.x_line, ln.y_line, label="Y=kx+m" ,color= "blue")
plt.title("Scatter plot of labelled data with line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()