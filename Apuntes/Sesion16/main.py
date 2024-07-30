from bs4 import BeautifulSoup  # Instalamos Beautiful Soup
import requests  # Para trabajar con live Website

# import lxml - En algunas webs es posible que necesitemos usar el parser de lxml

# --------- Trabajamos en local --------------

with open('website.html', encoding='utf-8') as file:  # Cargamos el HTML
    contenido = file.read()

# Parámetros: Texto, el parser('html.parser', 'lxml')
soup = BeautifulSoup(contenido, 'html.parser')
# Ahora podemos usar el html como un objeto de Python
print(soup.title)
print(soup.title.name)  # Nos da el nombre de la etiqueta usada
print(soup.title.string)  # Nos hacemos con la cadena que contiene la etiqueta title
print(soup.prettify())  # Imprime el html con el sangrado
print(soup.a)  # Te devuelve la primera etiqueta que encuentre de anclaje <a>

all_anchor = soup.find_all(name='a')  # Nos devuelve una lista con todos los enlaces
print(all_anchor)

for tag in all_anchor:  # Recorremos el listado
    print(tag.getText())  # Sacamos solo los textos
    print(tag.get('href'))  # Imprime los enlaces

cabecera = soup.find(name='h1', id='name')  # Nos lanza el primer h1 con el atributo id 'name' que encuentra
print(cabecera)

section_heading = soup.find(name='h3', class_='heading')  # Igual para el atributo class
print(section_heading)

# Podemos buscar un enlace concreto usando los CSS selectors
company_url = soup.select_one(selector='p a')  # Buscamos un enlace que esté dentro de un párrafo
print(company_url)
name = soup.select_one(selector='#name')  # Buscamos por el atributo id
print(name)
headings = soup.select('.heading')  # Listado con los que contienen la clase heading
print(headings)

# ------------- Live Website -----------------

# -------- 1. Conseguir el primer titular de las noticias ------------
response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text
print(yc_web_page)  # Muestra el HTML

soup2 = BeautifulSoup(yc_web_page, 'html.parser')  # Analizamos el HTML
# Inspeccionamos antes la web para ver la estructura y localizar los títulos.
primer_titulo = soup2.select_one('td .title a')  # Capturamos el primer título
print(primer_titulo)
name_primer_titulo = primer_titulo.getText()  # Mostramos el texto
print(name_primer_titulo)
article_link = primer_titulo.get('href')  # Mostramos solo el enlace
print(article_link)

article_upvote = soup2.select_one('span .score')  # Para mostrar los votos
print(article_upvote.getText())

# --------------- 2. Todos los titulares -------------
article_texts = []
article_links = []
titulos = soup2.select('td .title a')
for titulo in titulos:
    article_texts.append(titulo.getText())
    article_links.append(titulo.get('href'))

# Nos quedamos con la parte numérica de los votos, en vez de imprimir 320 points, imprimirá 320.
# y lo pasamos a entero
article_upvotes = [int(score.getText().split()[0]) for score in soup2.select('span .score')]

# Ahora buscamos el numero mayor y su indice
max_upvotes = max(article_upvotes)
indice_max_upvotes = article_upvotes.index(max_upvotes)

print(article_texts)
print(article_links)
print(article_upvotes)


