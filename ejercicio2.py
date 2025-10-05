import pandas as pd

Compras_v2 = pd.read_csv("data/Compras_v2.csv", sep=';')

num_cols = ['Edad', 'Salario', 'Compra', 'Deuda_tc']
for col in num_cols:
    if col in Compras_v2.columns:
        Compras_v2[col] = Compras_v2[col].astype(str).str.replace(',', '', regex=False)
        Compras_v2[col] = pd.to_numeric(Compras_v2[col], errors='coerce')

for col in ['Salario', 'Edad', 'Deuda_tc']:
    Compras_v2[col] = Compras_v2[col].fillna(Compras_v2[col].mean())

for col in ['Genero', 'Region', 'Compra']:
    mode_val = Compras_v2[col].mode()
    if not mode_val.empty:
        Compras_v2[col] = Compras_v2[col].fillna(mode_val[0])

Compras_v2['Compra'] = Compras_v2['Compra'].astype(int)

Compras_v2['Salario_mas_10'] = Compras_v2['Salario'] + 10

print("Ejercicio 2 completado: Variable 'Salario_mas_10' creada.")
print(Compras_v2)