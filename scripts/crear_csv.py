import pandas as pd

data = {
    "producto": ["mouse", "teclado", "monitor", "mouse"],
    "cantidad": [2, 1, 1, 3],
    "precio": [100, 200, 300, 100],
    "fecha": ["2026-01-10", "2026-01-11", "2026-02-05", "2026-02-10"]
}

df = pd.DataFrame(data)

df.to_csv("../datos/ventas.csv", index=False)

print("CSV creado correctamente")