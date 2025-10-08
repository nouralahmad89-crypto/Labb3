# main.py
import numpy as np
import matplotlib.pyplot as plt
import csv
import line_class as ln

# ===== Funktioner =====
def point_position(x_point, y_point, k, m):
    """
    Bestämmer om en punkt ligger ovanför (höger) eller under (vänster) 
    om linjen y = kx + m 
    Returnerar:
        0 om punkten ligger under/eller vänster om linjen
        1 om punkten ligger ovanför/eller höger om linjen
    """
    line_y = k * x_point + m
    if y_point > line_y:
        return 1
    else:
        return 0

# ===== Körbar kod =====
if __name__ == "__main__": # för att kunna importera bara point_position för VG uppgift
    # d) Klassificera alla punkter
    points = list(zip(ln.d1, ln.d2))
    labels = [point_position(p[0], p[1], ln.k, ln.m) for p in points]

    # e) Skapa labelled_data.csv
    with open("labelled_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x Values", "y Values", "label"])  # rubriker
        for p , label in zip(points, labels):
                writer.writerow([p[0], p[1], label])
    print("Filen 'labelled_data.csv' har skapats med etiketter (0/1)")

    # f) Visa graf med punkter och linje
    x_values = np.array([p[0] for p in points])
    y_values = np.array([p[1] for p in points])
    labels = np.array(labels)  # Konvertera till numpy-array

    upper_indx = np.where(labels == 1)  # punkter ovanför linjen
    lower_indx = np.where(labels == 0)  # punkter under linjen

    plt.figure(figsize=(7,5))
    plt.scatter(x_values[upper_indx], y_values[upper_indx], label="Data points above line", color="yellow", marker="*")
    plt.scatter(x_values[lower_indx], y_values[lower_indx], label="Data points lower line", color="green", marker="*")
    plt.plot(ln.x_line, ln.y_line, label="Y=kx+m", color="blue")
    plt.title("Scatter plot of labelled data with line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
