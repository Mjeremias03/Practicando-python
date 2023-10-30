import pandas as pd 

# datos = pd.read_csv("datoss.csv",encoding="utf-8")

datos = pd.read_csv("datoss.csv", encoding="latin-1")
# nombre = datos["Ciudad"]
print(datos)
datos.to_csv("datos_limpios.csv", index=False, encoding="latin-1")