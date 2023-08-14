import json
import pandas as pd

with open("3\dados_compras.json") as f:
    data = json.load(f)

for i in range(0, len(data)):
    print(data[i])

# Identifique a quantidade total de compras realizadas.
print(f"quantidade total de compras realizadas: {len(data)}")
