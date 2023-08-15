import requests
from bs4 import BeautifulSoup

# Solicitação GET para o URL do subreddit r/programming
response = requests.get("https://www.reddit.com/r/programming/.json")

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Obter os dados JSON da resposta
    data = response.json()

    # Obter a lista de postagens do campo "data" do JSON
    posts = data["data"]["children"]

    # Iterar sobre as três primeiras postagens
    for i in range(3):
        # Título, up votes e o link
        title = posts[i]["data"]["title"]
        upvotes = posts[i]["data"]["ups"]
        link = posts[i]["data"]["url"]

        # Informações da postagem
        print(f"Postagem {i+1}:")
        print(f"Título: {title}")
        print(f"Up votes: {upvotes}")
        print(f"Link: {link}")
        print()
else:
    # Mensagem de erro se a solicitação falhar
    print(f"Erro: {response.status_code}")
