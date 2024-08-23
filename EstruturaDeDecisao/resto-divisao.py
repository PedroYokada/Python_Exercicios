#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).


num_inteiro = int(input("Digite um numero inteiro: "))

if num_inteiro % 2 == 0:
  print(f"o numero {num_inteiro} é par!")
else:
  print(f"o numero {num_inteiro} é impar!")