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