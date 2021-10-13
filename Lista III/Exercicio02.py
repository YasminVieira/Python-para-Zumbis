# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações:

usuario = input('Digite o seu usuário: ')
senha = input('Digite a sua senha: ')
while usuario == senha:
    print('Usuario igual a senha. Por favor digite novamente')
    usuario = input('Digite o seu usuário: ')
    senha = input('Digite a sua senha: ')
else:
    print('Usuário e senha válidos. Bem-vindo!')
