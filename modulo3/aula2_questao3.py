idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (true/false): ") == "true"
vitorias = int(input("Quantas vezes você venceu um jogo? "))

print(16 <= idade <= 18 and jogou_3_jogos and vitorias >= 1)