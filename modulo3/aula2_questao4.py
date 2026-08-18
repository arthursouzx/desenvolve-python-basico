classe = input("Digite a classe (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

resultado = (
    (classe == "guerreiro" and forca >= 15 and magia <= 10)
    or
    (classe == "mago" and forca <= 10 and magia >= 15)
    or
    (classe == "arqueiro" and forca > 5 and magia > 5 and forca <= 15 and magia <= 15)
)

print(resultado)