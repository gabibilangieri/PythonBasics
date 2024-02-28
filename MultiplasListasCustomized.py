nome = []
telefone = []
cidade = []
regiao = []
resposta = "S"
while resposta == "S":
    nome.append(input("Nome: "))
    telefone.append(float(input("Telefone: ")))
    cidade.append(input("Cidade: "))
    regiao.append(input("Região: "))
    resposta = input("Digite \"S\"para continuar: ").upper()

for indice in range(0, len(nome)):
    print("\nNome..: ", (indice + 1))
    print("Nome.........: ", nome[indice])
    print("Telefone........: ", telefone[indice])
    print("Cidade.......: ", cidade[indice])
    print("Região.: ", regiao[indice])
