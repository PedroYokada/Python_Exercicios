#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

media = float(nota1+nota2+nota3+nota4)/4
media = round(media, 2)

print("A média das quatro notas é de: ", media)