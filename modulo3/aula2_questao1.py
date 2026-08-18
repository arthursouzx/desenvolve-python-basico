#entrada de dados
#idade de juliana
#idade de cris
idade_juliana = int(input())
print(idade_juliana)
idade_cris = int(input())
print(idade_cris)

#processamento
#True se ambos forem maior de idade
#<exp1> Juliana é maior de idade
#<exp2> Cris é maior de idade
#<exp1> and <exp2>
#False em qualquer outro caso
pode_entrar = idade_juliana >= 18 and idade_cris >= 18

#saída
print(pode_entrar)