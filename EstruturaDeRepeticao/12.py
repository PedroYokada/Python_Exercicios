#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo

tabuada = int(input("Escolha a tabuada de 1 a 10: "))

num_vezes = 0

print(f"Tabuada do numero: {tabuada}")

for i in range(0,11):
  print(f"{tabuada} x {num_vezes} = {tabuada * num_vezes}")
  num_vezes = num_vezes + 1