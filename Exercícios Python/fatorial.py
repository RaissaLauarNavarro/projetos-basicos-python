numero = int(input("Digite o valor de n: "))

resultado = 1
counter = 1

while counter <= numero:
    resultado *= counter
    counter += 1

print(resultado)
