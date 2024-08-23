""" Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
 O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
 par ou ímpar; positivo ou negativo; inteiro ou decimal. """
 
import math
 
num1 = float(input("Digite o primeiro numero inteiro ou decimal: "))
num2 = float(input("Digite o segundo numero inteiro ou decimal: "))
operacao = (input("1 - SOMA , 2 - SUBTRAÇÃO 3 - MULTIPLICACAO  4 - DIVISAO: "))

match operacao:
  
  case "1":
    num3 = (num1 + num2)
  case "2":
    num3 = (num1 - num2)
  case "3":
    num3 = (num1 * num2)
  case "4":
    if num2 != 0:
         num3 = num1/num2
    else:
      print("Divisão por zero não é permitido!")
      exit()
  case _:
      print("Operação inválida!")
      exit()
      
if num3 < 0:
  print(f"o numero {num3} é negativo!")
else:
  print(f"o numero {num3} é positivo!")
  
if num3 == round(num3):
  print(f"o numero {num3} é inteiro!")
else:
  print(f"o numero {num3} é decimal!")
    
if num3 % 2 == 0:
  print(f"o numero {num3} é par!")
else:
  print(f"o numero {num3} é impar!")
  


