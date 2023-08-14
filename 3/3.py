import json
import pandas as pd

with open("3\dados_compras.json") as f:
    data = json.load(f)

df = pd.DataFrame(
    columns=["Login", "Idade", "Sexo", "Item ID", "Nome do item", "Valor"]
)

for i in range(0, len(data)):
    currentitem = data[i]
    df.loc[i] = [
        data[i]["Login"],
        data[i]["Idade"],
        data[i]["Sexo"],
        data[i]["Item ID"],
        data[i]["Nome do Item"],
        data[i]["Valor"],
    ]

# Identifique a quantidade total de compras realizadas.
print(df)
print(f"quantidade total de compras realizadas: {len(data)}")
