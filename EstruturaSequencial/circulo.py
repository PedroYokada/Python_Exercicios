#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input("Insira o valor do raio: "))

area_circulo = float(math.pi * (raio * raio))

area_circulo = round(area_circulo, 2)

print("A area do circulo é de: ", area_circulo, "cm")