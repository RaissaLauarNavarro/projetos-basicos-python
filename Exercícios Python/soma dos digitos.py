numero = int(input("Digite um número inteiro: "))
resposta = 0

while (numero > 0):
    resto = numero % 10
    numero = (numero-resto)/10
    resposta = resposta+resto

print(int(resposta))
