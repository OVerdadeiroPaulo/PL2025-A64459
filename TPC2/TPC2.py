import os

def ler_dataset(nome_arquivo):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(script_dir, nome_arquivo)

    with open(caminho_completo, encoding='utf-8') as f:
        linhas = f.readlines()

    cabecalho = linhas[0].strip().split(';')
    dados = []

    buffer = ""
    for linha in linhas[1:]:
        linha = linha.strip()
        if not linha:
            continue  

        buffer += " " + linha  
        partes = buffer.split(';')

        if len(partes) >= len(cabecalho):  
            while len(partes) > len(cabecalho):
                partes[1] += ';' + partes.pop(2)  
            dados.append(dict(zip(cabecalho, partes)))
            buffer = ""  

    return dados

def compositores_ordenados(dados):
    return sorted(set(obra['compositor'] for obra in dados))

def distribuicao_por_periodo(dados):
    dist = {}
    for obra in dados:
        periodo = obra['periodo']
        dist[periodo] = dist.get(periodo, 0) + 1
    return dist

def obras_por_periodo(dados):
    dicionario = {}
    for obra in dados:
        periodo = obra['periodo']
        nome_obra = obra['nome']
        if periodo not in dicionario:
            dicionario[periodo] = []
        dicionario[periodo].append(nome_obra)

    for periodo in dicionario:
        dicionario[periodo].sort()
    return dicionario

if __name__ == "__main__":
    dados = ler_dataset("obras.csv")  

    print("Compositores ordenados:")
    for compositor in compositores_ordenados(dados):
        print(compositor)

    print("\nDistribuição por período:")
    for periodo, contagem in distribuicao_por_periodo(dados).items():
        print(f"{periodo}: {contagem}")

    print("\nObras por período:")
    obras_dict = obras_por_periodo(dados)
    for periodo, obras in obras_dict.items():
        print(f"{periodo}:")
        for obra in obras:
            print(f"  - {obra}")