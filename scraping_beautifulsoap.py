import csv
import requests
from bs4 import BeautifulSoup

# URL da página que você deseja fazer scraping
url = "https://www.amazon.com.br/s?k=cadeira+de+escritorio&crid=399EITZ668JMX&sprefix=cadeira+%2Caps%2C186&ref=nb_sb_ss_ts-doa-p_1_8"

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre os elementos HTML que contêm os títulos de produtos e preços
    products = soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")
    prices = soup.find_all("span", class_="a-price-whole")
    prices_fraction = soup.find_all("span", class_="a-price-fraction")
    juros = soup.find_all("span", class_="a-size-base a-color-secondary")
    estrelas = soup.find_all("span", class_="a-size-base s-underline-text")

    # Cria o arquivo CSV com codificação UTF-8
    file = open('precos_cadeiraEscritorio.csv', 'w', newline='')

    writer = csv.writer(file)
    headers = ['Produto', 'Preço', 'Juros', 'Estrelas']  # Adicionando uma coluna para "Preço"
    writer.writerow(headers)

    # Loop pelos elementos e imprimir os títulos e preços
    for product, price, fraction, juro, estrela in zip(products, prices, prices_fraction, juros, estrelas):
        product_text = product.text.strip()
        juros_text = juro.text.strip()
        price_text = price.text.strip() + fraction.text.strip()  # Concatena preço e fração
        estrelas = estrela.text.strip()

        print("Produto:", product_text)
        print("Preco:", price_text)
        print("Juros:", juros_text)
        print("Estrelas:", estrelas)

        # Cada produto e preço
        row = [product_text, price_text, juros_text, estrelas]

        # Salva os dados no arquivo CSV
        writer.writerow(row)

    file.close()

else:
    print("Falha ao acessar a página:", response.status_code)
