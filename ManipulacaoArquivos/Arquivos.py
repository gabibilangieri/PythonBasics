with open("economic-indicators.csv", "r") as arquivos:
    total=0
    for linha in arquivos.readlines() [1:-1]:
        total=total+float(linha.split(",") [3])
    print ("O total de voos é: ", total)
