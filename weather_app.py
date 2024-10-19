import requests 
from bs4 import BeautifulSoup 
def ClimaApp():
    city = input("Digite o nome da cidade: \n")

    pesquisa = f"Clima em " + city + ":\n" 

    url = f"https://www.google.com/search?&q={pesquisa}"

    # Capturando a resposta do site
    resposta = requests.get(url) 

    # Buscando a informação do clima na página
    s = BeautifulSoup(resposta.text, "html.parser")

    # Extraindo e printando a temperatura atual
    update = s.find("div", class_="BNeawe").text
    print(update) 

ClimaApp() 