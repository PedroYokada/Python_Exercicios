#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira a altura de uma pessoa: "))
peso_ideal = float((72.7*altura) - 58)

peso_ideal = round(peso_ideal,2)

print("O peso ideal desta pessoa é de: ", peso_ideal, "kg")