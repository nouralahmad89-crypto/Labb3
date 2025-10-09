# main.py
import numpy as np
import matplotlib.pyplot as plt
import csv
from line_class import get_data

# === Läsa in data ===
path = "unlabelled_data.csv"
d1, d2 = get_data(path)

# Konvertera till numpy-arrays
x = np.array(d1)
y = np.array(d2)

# Beräkna linjen som delar punkterna 
x_val = np.mean(x)
y_val = np.mean(y)
"""När x=0 => m=y , nu har vi två punkter ( x_val, y_val ), (0,m)
räkan m värde: k = x_val-0 / y_val-m =>  m = x_val + y_val"""
k = -1
m = x_val + y_val  # linje nära datasetets centrum

x_line = np.linspace(min(x), max(x), 100)
y_line = k * x_line + m

# ===== Funktioner =====
def draw_line_p(xl, yl, k_värde, m_värde, xp, yp):
    plt.figure(figsize=(7,5))
    plt.scatter(xp, yp, label="Data points", color="red", marker="*")
    plt.plot(xl, yl, label=f"Y={k_värde}x+{m_värde:.2f}", color="blue")
    plt.title("Scatter plot of data with line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def point_position(x_point, y_point, k, m):
    """Returnerar: 0 om punkten ligger under/eller vänster om linjen
    1 om punkten ligger ovanför/eller höger om linjen"""
    if y_point > k*x_point + m:
       return 1
    else:
       return 0

def classify_points_and_get_labels():
    """Returnerar x_values, y_values och labels för dataset"""
    points = list(zip(d1, d2))
    labels = np.array([point_position(p[0], p[1], k, m) for p in points])
    x_values = np.array([p[0] for p in points])
    y_values = np.array([p[1] for p in points])
    return x_values, y_values, labels

def draw_classified(xl, yl, k_värde, m_värde, xp, yp, my_label):
    # Lägg till 0.5 marginal runt datapunkterna på x- och y-axeln
    x_min, x_max = min(xp) - 0.5, max(xp) + 0.5 
    y_min, y_max = min(yp) - 0.5, max(yp) + 0.5
    upper_indx = np.where(my_label == 1)
    lower_indx = np.where(my_label == 0)
    plt.figure(figsize=(7,5))
    plt.scatter(xp[upper_indx], yp[upper_indx], label="Above line", color="yellow", marker="*")
    plt.scatter(xp[lower_indx], yp[lower_indx], label="Below line", color="green", marker="*")
    plt.plot(xl, yl, label=f"Y={k_värde}x+{m_värde:.2f}", color="blue")
    plt.title("Scatter plot of labelled data with line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True)
    plt.show()

# ===== Körbar kod när scriptet körs direkt =====
if __name__ == "__main__":
    x_values, y_values, labels = classify_points_and_get_labels()

    # Skriv labelled_data.csv
    with open("labelled_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x Values", "y Values", "label"])
        for p, label in zip(zip(x_values, y_values), labels):
            writer.writerow([p[0], p[1], label])
    print("Filen 'labelled_data.csv' har skapats med etiketter (0/1)")

    # Visa graf med klassificerade punkter
    draw_classified(x_line, y_line, k, m, x_values, y_values, labels)
