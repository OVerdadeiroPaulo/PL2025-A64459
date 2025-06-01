import re
import sys

def markdown_para_html(linhas):
    resultado = []
    dentro_lista = False

    for linha in linhas:
        linha = linha.rstrip()

        # Cabeçalhos
        if linha.startswith("### "):
            resultado.append(f"<h3>{linha[4:]}</h3>")
            continue
        elif linha.startswith("## "):
            resultado.append(f"<h2>{linha[3:]}</h2>")
            continue
        elif linha.startswith("# "):
            resultado.append(f"<h1>{linha[2:]}</h1>")
            continue

        # Listas numeradas
        if re.match(r'\d+\.\s', linha):
            if not dentro_lista:
                resultado.append("<ol>")
                dentro_lista = True
            conteudo = re.sub(r'^\d+\.\s+', '', linha)
            resultado.append(f"<li>{conteudo}</li>")
            continue
        elif dentro_lista:
            resultado.append("</ol>")
            dentro_lista = False

        # Links: [texto](url)
        linha = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', linha)

        # Imagens: ![alt](url)
        linha = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', linha)

        # Bold: **texto**
        linha = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', linha)

        # Itálico: *texto*
        linha = re.sub(r'\*(.+?)\*', r'<i>\1</i>', linha)

        resultado.append(linha)

    if dentro_lista:
        resultado.append("</ol>")

    return resultado

if __name__ == "__main__":
    # Lê linhas do stdin (pode redirecionar com '< ficheiro.md')
    with open("mkdwn.md", encoding='utf-8') as f:
        linhas = f.readlines()
    html = markdown_para_html(linhas)
    with open("exemplo.html", "w", encoding="utf-8") as f:
        f.write("<html><body>\n")
        for linha in html:
            f.write(linha + "\n")
        f.write("</body></html>\n")

    print("Conversão completa: ficheiro 'exemplo.html' criado.")
