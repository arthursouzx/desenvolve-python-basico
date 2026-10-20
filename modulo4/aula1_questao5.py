n = int(input("Quantas pessoas responderam? "))
soma = 0
for i in range(n):
    idade = int(input("Digite a idade: "))
    soma = soma + idade
media = soma / n
print("A média das idades é:", media)
