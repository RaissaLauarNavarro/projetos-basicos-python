numero = int(input("Digite um número: "))
teste1 = numero%5
teste2 = numero%3

if teste1 == 0 and teste2 == 0:
   print("FizzBuzz")
else:
    print(numero)
