
import csv

moedas = {}

# Carregar os dados do arquivo
with open("moedas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        codigo = linha[0]
        nome = linha[2]
        cotacao = float(linha[3])

        moedas[codigo] = {
            "nome": nome,
            "cotacao": cotacao
        }

# Solicitar os dados ao usuário
valor = float(input("Digite o valor em reais: R$ "))
destino = input("Digite o código da moeda de destino: ").upper()

# Fazer a conversão
if destino in moedas:
    nome = moedas[destino]["nome"]
    cotacao = moedas[destino]["cotacao"]

    convertido = valor / cotacao

    print("Moeda:", nome)
    print("Valor convertido:", convertido)

else:
    print("Moeda não encontrada!")