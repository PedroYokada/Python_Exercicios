""" Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar 
com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. """

notas = int(input("Insira um valor para sacar no minimo de 10 R$ até 600 R$: "))

if notas < 10 or notas > 600:
  print("Valor inválido")
else:
  nota_100 = notas // 100
  notas %= 100
  
  nota_50 = notas // 50
  notas %= 50
  
  nota_20 = notas // 20
  notas %= 20
  
  nota_10 = notas // 10
  notas %= 10
  
  nota_5 = notas // 5
  notas %= 5
  
  nota_1 = notas // 1
  notas %= 1
  
  print(f"Quantidades de nota(s) sacada(s) de 100R$: {nota_100}")
  print(f"Quantidades de nota(s) sacada(s) de 50R$: {nota_50}")
  print(f"Quantidades de nota(s) sacada(s) de 20R$: {nota_20}")
  print(f"Quantidades de nota(s) sacada(s) de 10R$: {nota_10}")
  print(f"Quantidades de nota(s) sacada(s) de 5R$ {nota_5}")
  print(f"Quantidades de nota(s) sacada(s) de 1R$ {nota_1}")
  
  
  

 
  

