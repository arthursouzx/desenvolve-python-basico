distancia = float(input("Digite a distancia em km: "))
peso = float(input("Digite o peso em kg: "))

if distancia <= 100:
    preco_kg =1
elif distancia <= 300:
    preco_kg = 1.50
else:
    preco_kg = 2

frete = peso * preco_kg

if peso > 10:
    frete = frete + 10

print("Valor do frete:R$", frete)