filmes = [
    {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
    {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
    {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6},
]

# Média das avaliações

avaliacoes = [filme["avaliacao"] for filme in filmes]
soma = sum(avaliacoes)
media = soma / 3
print("A média das avaliaçoes dos filmes é:", (media))

# Titulo do filme com maior avaliação
filme_maior_avaliacao = max(filmes, key=lambda x: x["avaliacao"])
print(f"O título do filme com a maior avaliação é {filme_maior_avaliacao['titulo']}")

# Ano de lançamento do filme com menor avaliação
filme_menor_avaliacao = min(filmes, key=lambda x: x["avaliacao"])
print(
    f"O ano de lançamento do filme com menor avaliação é {filme_menor_avaliacao['ano']}"
)
