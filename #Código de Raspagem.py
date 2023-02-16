#Código de Raspagem
import requests
from bs4 import BeautifulSoup

# URL do site a ser raspado
url = "https://www.example.com/blog"

# Faz uma requisição à URL e obtém o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisa o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extrai todas as URLs de artigos
    article_links = [link.get("href") for link in soup.find_all("a") if link.get("href").startswith("/article")]

    # Imprime as URLs extraídas
    print(article_links)
else:
    # Imprime uma mensagem de erro
    print("Não foi possível acessar o site")
