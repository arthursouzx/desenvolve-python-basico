n = int(input())
coelhos = 0
ratos = 0
sapos = 0
for i in range(n):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    if tipo == "C":
        coelhos = coelhos + quantidade
    elif tipo == "R":
        ratos = ratos + quantidade
    elif tipo == "S":
        sapos = sapos + quantidade
total = coelhos + ratos + sapos
print("Total:", total, "cobaias")
print("Total de coelhos:", coelhos)
print("Total de ratos:", ratos)
print("Total de sapos:", sapos)
print("Percentual de coelhos:", format(coelhos / total * 100, ".2f"), "%")
print("Percentual de ratos:", format(ratos / total * 100, ".2f"), "%")
print("Percentual de sapos:", format(sapos / total * 100, ".2f"), "%")