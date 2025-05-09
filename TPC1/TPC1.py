import sys

is_on = True
soma = 0

def soma_dos_numeros(linha):
    global soma, is_on
    numero_atual = ''
    i = 0
    while i < len(linha):
        c = linha[i]

        if linha[i:i+2].lower() == "on":
            is_on = True
            i += 2
            continue
        elif linha[i:i+3].lower() == "off":
            is_on = False
            i += 3
            continue

        if c.isdigit():
            numero_atual += c
        else:
            if numero_atual:
                if is_on:
                    soma += int(numero_atual)
                numero_atual = ''
            if c == '=':
                if numero_atual:
                    if is_on:
                        soma += int(numero_atual)
                    numero_atual = ''
                print(f">> {soma}")

        i += 1

    if numero_atual:
        if is_on:
            soma += int(numero_atual)
            print(f">> {soma}")

if __name__ == "__main__":
    for linha in sys.stdin:
        print(linha, end='')
        soma_dos_numeros(linha)
    print(f">> {soma}")