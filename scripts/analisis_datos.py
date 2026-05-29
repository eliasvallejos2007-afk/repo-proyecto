import pandas as pd

df = pd.read_csv("datos/ventas.csv")

# Ventas totales
df["total"] = df["cantidad"] * df["precio"]
print("Ventas totales:", df["total"].sum())

# Producto más vendido
print("\nProducto más vendido:")
print(df.groupby("producto")["cantidad"].sum())

# Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
ventas_mes = df.groupby(df["fecha"].dt.month)["total"].sum()

print("\nVentas por mes:")
print(ventas_mes)
