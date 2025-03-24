import csv
import os
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# URL do Mercado Livre
URL = "https://www.mercadolivre.com.br/"

CSV_FILE = "ATV03/produtos.csv"

# Iniciar o WebDriver
driver = webdriver.Chrome()

def salvar_produto_csv(produto, preco, caminho_arquivo=CSV_FILE):
    """Salva um único produto no arquivo CSV."""
    criar_arquivo_csv(caminho_arquivo)  # Criar o arquivo caso não exista

    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([produto, preco])

    print(f"Salvo: {produto} - {preco}")

def criar_arquivo_csv(caminho_arquivo):
    """Cria o arquivo CSV caso não exista e adiciona o cabeçalho."""
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome do Produto", "Preço"])  # Cabeçalho
        print(f"Arquivo {caminho_arquivo} criado com sucesso.")

def formatar_preco(texto):
    match = re.search(r"(\d+(?:\.\d{3})*(?:,\d{2})?)", texto) 
    return f"R$ {match.group(1)}" if match else "Preço não disponível"

try:
    # Acessar o Mercado Livre
    driver.get(URL)
    time.sleep(2)

    # Localizar a barra de pesquisa e pesquisar "Celular"
    search_box = driver.find_element(By.ID, "cb1-edit")
    search_box.send_keys("Celular")
    search_box.send_keys(Keys.RETURN)

    # Aguardar os resultados carregarem
    time.sleep(3)

    # Percorrer os 5 primeiros produtos
    for i in range(5):
        # Buscar os elementos novamente para evitar o erro StaleElementReferenceException
        products = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")

        if i >= len(products):
            print("Menos de 5 produtos encontrados.")
            break

        # Encontrar o link do produto
        link_element = products[i].find_element(By.TAG_NAME, "a")
        product_url = link_element.get_attribute("href")

        # Acessar o produto
        driver.get(product_url)
        print(f"Acessando produto {i + 1}: {driver.title}")
        get_valor = driver.find_element(By.CLASS_NAME, "andes-money-amount__fraction")


        # Pega os valores
        produto_name = driver.title
        produto_price_no_formatted = get_valor.text

        product_price_formatted = formatar_preco(get_valor.text)

        # Salva na planilha
        salvar_produto_csv(produto= produto_name, preco= product_price_formatted)

        # Esperar um pouco para simular a leitura da página
        time.sleep(3)

        # Voltar para os resultados da pesquisa
        driver.back()
        time.sleep(3)  # Esperar a página carregar novamente

finally:
    # Fechar o navegador
    driver.quit()
