def cadastrar_catalogo(nome_arquivo):
    catalogo = []
    with open(nome_arquivo, "rt", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            infos = linha.split(",")

            titulo = infos[0]
            autor = infos[1]
            ano = int(infos[2])
            genero = infos[3]
            paginas = int(infos[4])

            ebook = {
                "titulo" : titulo,
                "autor" : autor,
                "ano" : ano,
                "genero" : genero,
                "paginas" : paginas
            }

            catalogo.append(ebook)
            
    return catalogo

def listar_genero(catalogo):

    generos = []

    for ebook in catalogo:
        if ebook["genero"] not in generos:
            generos.append(ebook["genero"])

    print("Gêneros dos livros cadastrados no catálogo: \n")

    for gen in generos:
        print(f"—> {gen}")

    genero_solicitado = input("\nInforme o gênero que gostaria de consultar: ")

    print()

    for ebook in catalogo:
       if ebook["genero"].lower() == genero_solicitado.lower():
           print(f"Título do Livro: {ebook["titulo"]} | Autor: {ebook["autor"]}")

def calcular_media(catalogo):
    total_paginas = 0
    contador = 0

    for ebook in catalogo:
        total_paginas += ebook["paginas"]
        contador += 1

    media = total_paginas / contador

    print("Média de páginas dos livros do catálogo: \n")
    print(f"{media} páginas")

def ordenar_ano(catalogo):
    mais_antigo = catalogo[0]

    for ebook in catalogo:
        if ebook["ano"] < mais_antigo["ano"]:
            mais_antigo = ebook

    print("Livro mais antigo: \n")
    print(f"Título do Livro: {mais_antigo["titulo"]} | Ano de Publicação: {mais_antigo["ano"]} ")

def limitar_paginas(catalogo):
    limitador = int(input("Informe a quantidade mínima de páginas para a consulta: "))

    print(f"\nLivros do catálogo com mais de {limitador} páginas:\n")

    for ebook in catalogo:
        if ebook["paginas"] >= limitador:
            print(f"Título do Livro: {ebook["titulo"]} | Número de Páginas: {ebook["paginas"]}")

def ordernar_titulo(catalogo):
    catalogo_ordenado = catalogo[:]

    tamanho = len(catalogo_ordenado)
    trocou = True
    
    while trocou:
        trocou = False

        for i in range(tamanho - 1):
            if catalogo_ordenado[i]["titulo"].lower() > catalogo_ordenado[i + 1]["titulo"].lower():
                suporte = catalogo_ordenado[i]
                catalogo_ordenado[i] = catalogo_ordenado[i + 1]
                catalogo_ordenado[i + 1] = suporte
                trocou = True

    print("Catálogo de livros ordenado por ordem alfabética crescente:\n")

    for ebook in catalogo_ordenado:
        print(f"Título do Livro: {ebook["titulo"]} | Autor: {ebook["autor"]}")
    
    print()

nome_arquivo = "catalogo_ebooks.txt"
catalogo = cadastrar_catalogo(nome_arquivo) 
listar_genero(catalogo) 
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
calcular_media(catalogo) 
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
ordenar_ano(catalogo)   
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
limitar_paginas(catalogo) 
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
ordernar_titulo (catalogo) 