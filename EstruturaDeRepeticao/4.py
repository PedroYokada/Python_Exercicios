""" Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. """

paisA = float(80.000)
taxa1 = 0.03
paisB = float(200.000)
taxa2 = 0.015
num_anos = 0

while paisA < paisB:
  paisA = paisA + (paisA * taxa1) 
  paisB = paisB + (paisB * taxa2) 
  num_anos += 1


print(f"A população do País A é de: {paisA:.2f} milhões de habitantes")
print(f"A população do País B é de: {paisB:.2f} milhões de habitantes")
print(f"O numero de anos para do País A superar País B é de: {num_anos} anos ")
