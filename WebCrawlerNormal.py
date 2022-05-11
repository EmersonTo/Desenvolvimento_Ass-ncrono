from bs4 import BeautifulSoup
from requests import get
from time import time

inicio = time()
resposta = get('https://pt.wikipedia.org/wiki/Sociedade_Esportiva_Palmeiras#Hist%C3%B3rico_Categoria_Master')
tags = BeautifulSoup(resposta.text,'html5lib')
nome_pagina = tags.find("h1",attrs={"class" : "firstHeading mw-first-heading"})
print(f"Página principal: {nome_pagina.text}")
paginas =  tags.find_all("a",href = True)

visitar = []
for pagina in paginas:
    visitar.append(pagina.get('href'))

comeca_com = "/wiki/"
links =list(filter(lambda x: x.startswith(comeca_com), visitar))

print(f"Total de Páginas a Visitar: {len(visitar)}")

print(f"Página principal: {nome_pagina.text}")
for link in links:
    resposta_sec = get("https://pt.wikipedia.org/" + link)
    tags_sec = BeautifulSoup(resposta_sec.text,'html5lib')
    nome_pagina_sec = tags_sec.find("h1",attrs={"class" : "firstHeading mw-first-heading"})
    print(f"Página secundária:  {nome_pagina_sec.text}")

termino = time()

print(f"Tempo total da execução:{abs(int(termino - inicio))} segundos")