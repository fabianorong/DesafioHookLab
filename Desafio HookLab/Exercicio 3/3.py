import json
import pandas as pd
import matplotlib.pyplot as plt

with open("Desafio HookLab\Exercicio 3\dados_compras.json") as f:
    data = json.load(f)

tabela = pd.DataFrame(data)

tabela_agrupada = (
    tabela.groupby("Login")
    .agg(
        {
            "Idade": "unique",
            "Sexo": "unique",
            "Item ID": "unique",
            "Nome do Item": "unique",
            "Valor": "sum",
        }
    )
    .reset_index()
)
print(tabela_agrupada)

# Identifique a quantidade total de compras realizadas.
print(f"Quantidade total de compras realizadas: {len(tabela_agrupada)}")

# Calcule a média, o valor mínimo e máximo gasto por compra.
soma = tabela_agrupada["Valor"].sum()
media = soma / (len(tabela_agrupada))
print(f"Valor medio gasto por compra: {media}")

max_valor = tabela_agrupada["Valor"].max()
print(f"Valor maximo gasto por compra: {max_valor}")

min_valor = tabela_agrupada["Valor"].min()
print(f"Valor minimo gasto por compra: {min_valor}")

# Determine o produto mais caro e o produto mais barato.

df = tabela.explode("Valor").explode("Item ID").explode("Nome do Item")
max_valor = df["Valor"].max()
min_valor = df["Valor"].min()

produto_mais_caro = df.loc[
    df["Valor"] == max_valor, ["Valor", "Item ID", "Nome do Item"]
]

produto_mais_barato = df.loc[
    df["Valor"] == min_valor, ["Valor", "Item ID", "Nome do Item"]
]

df2 = produto_mais_caro.drop_duplicates("Item ID", keep="first")
df3 = produto_mais_barato.drop_duplicates("Item ID", keep="first")

print("Produto mais caro:")
print(df2)
print("Produto mais barato:")
print(df3)

# Segmentação por Gênero
tabela_agrupada_genero = (
    tabela.groupby("Sexo")
    .agg(
        {
            "Valor": "sum",
        }
    )
    .reset_index()
)
print("Valor total gasto em compras por gênero:")
print(tabela_agrupada_genero)

# Calcular a frequência de cada sexo na coluna de Sexo
freq_sexo = tabela_agrupada["Sexo"].value_counts()
# Calcular a porcentagem de cada sexo na coluna de Sexo
perc_sexo = freq_sexo.apply(lambda x: x / len(tabela_agrupada) * 100)
# Converter a série em um dataframe e mostrar as colunas de Sexo e Porcentagem
dist_sexo = perc_sexo.to_frame().reset_index()
dist_sexo.columns = ["Sexo", "Porcentagem"]
print("distribuição de gênero entre os consumidores:")
print(dist_sexo)

# Gerar um gráfico de pizza Distribuição de Gênero entre os Consumidores
dist_sexo.plot(kind="pie", y="Porcentagem", labels=dist_sexo["Sexo"], autopct="%1.1f%%")
plt.title("Distribuição de Gênero entre os Consumidores")
plt.show()

# Gráfico de barras Valor total gasto em compras por gênero
tabela_agrupada_genero.plot(kind="bar", x="Sexo", y="Valor")
plt.title("Valor total gasto em compras por gênero")
plt.show()

# Grafico de barras para quantidades compradas por item ID
tabela_agrupado_item = tabela.groupby("Item ID").count()

tabela_agrupado_item.plot(kind="bar", y="Login")
plt.title("Quantidade de cada Item comprado")
plt.xlabel("Item ID")
plt.ylabel("Quantidade")
plt.legend().remove()
plt.tight_layout()
plt.show()
