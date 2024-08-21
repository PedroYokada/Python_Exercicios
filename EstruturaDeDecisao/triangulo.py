""" Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes; """

v1 = float(input("Insira o valor do primeiro lado do triangulo: "))
v2 = float(input("Insira o valor do segundo lado do triangulo: "))
v3 = float(input("Insira o valor do terceiro lado do triangulo: "))

if (v1 + v2) > v3 and (v1 + v3) > v3 and (v2 + v3) > v1:
  if v1 == v2 == v3:
        print(f"Triângulo Equilátero: três lados iguais, lado 1: {v1:.2f}, lado 2: {v2:.2f}, lado 3: {v3:.2f}")
  elif v1 != v2 != v3 != v1:
        print(f"Triângulo Escaleno: três lados diferentes, lado 1: {v1:.2f}, lado 2: {v2:.2f}, lado 3: {v3:.2f}")
  else:
        print(f"Triângulo Isósceles: quaisquer dois lados iguais, lado 1: {v1:.2f}, lado 2: {v2:.2f}, lado 3: {v3:.2f}")
else:
    print("Os valores inseridos não formam um Triângulo.")