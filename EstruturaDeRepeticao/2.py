""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while nome == senha:
  print("Erro, insira seu nome e senha novamente!")
  nome = input("Digite seu nome: ")
  senha = input("Digite sua senha: ")


print(f"seu nome é: {nome}, sua senha é: {senha}")