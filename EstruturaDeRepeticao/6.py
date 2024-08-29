""" Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa 
para que ele mostre os números um ao lado do outro. """
num = 1

while num <= 20:
  num = num + 1
  print(num - 1)
  
num2 = 1

while num2 <= 20:
  num2 = num2 + 1
  print(num2 - 1, end = " ")
  
#end = " " é um argumento usado para imprimir coisas na mesma linha