""" Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; """

def nome_verificar(s):
    return len(s) >= 3

nome = input("Insira seu nome: ").upper()

while not nome_verificar(nome):
    print("Nome inválido, digite novamente!")
    nome = input("Insira seu nome: ").upper()

idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
  print("Idade inválida, digite novamente!")
  idade = int(input("Digite sua idade: "))
  
salario = float(input("Digite seu salario: "))

while salario <= 0.00:
  print("salario inválido, digite novamente!")
  salario = float(input("Digite seu salario: "))
  
sexo = input("Digite seu sexo - F-Feminino/M - Masculino: ").upper()

while sexo != "F" and sexo != "M":
  print("sexo inválido, digite novamente!")
  sexo = input("Digite seu sexo - F-Feminino/M - Masculino: ").upper()
  
estado = input("Digite seu estado civil - S - Solteiro/ C-Casado/ - V-Viuvo/ - D-Divorciado: ").upper()

while estado != "S" and estado != "C" and estado != "V" and estado != "D":
  print("Estado civil inválido, digite novamente!")
  estado = input("Digite seu estado civil - S - Solteiro/ C-Casado/ - V-Viuvo/ - D-Divorciado: ").upper()
  

print(f"Seu nome é: {nome}, Idade: {idade}, Salario: {salario:4.2f}R$, Sexo: {sexo} e Estado civil: {estado}")