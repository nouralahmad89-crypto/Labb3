# Linjär klassificering - Laboration

Detta projekt är en laboration i linjär klassificering.  
Syftet är att träna en enkel klassificeringsmodell på given data och spara resultaten i en CSV-fil.

## Innehåll
Projektet innehåller följande filer:
- `main.py` – Python-programmet som läser in datapunkter, ritar en linje och klassificerar varje punkt som ovanför eller under linjen.
- `labelled_data.csv` – Datafil som skapats av programmet, innehåller samma punkter men med en extra kolumn för etikett (0 = under linjen, 1 = ovanför linjen).
- `report.ipynb` – En Jupyter Notebook med förklaringar och visualiseringar.

## Förklaring av programmet

1. Läser in punkterna från CSV-filen.
2. Plottar punkterna i en scatterplot.
3. Beräknar en linje som delar punkterna så jämnt som möjligt (med hjälp av medelvärden för x och y).
4. Använder en funktion `point_position()` för att bestämma om varje punkt ligger **ovanför/under** (eller vänster/höger) om linjen.
5. Sparar resultatet i en ny fil `labelled_data.csv` med en extra kolumn `label`:
   - `0` = punkten ligger under/vänster om linjen  
   - `1` = punkten ligger ovanför/höger om linjen  

