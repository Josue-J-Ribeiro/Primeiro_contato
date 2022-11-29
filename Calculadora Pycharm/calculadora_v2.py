# Calculadora em Python

print("\n******************* Python Calculator *******************")

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def percentage(x, y):
	return + x * y / 100

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Porcentagem")
escolha = input("\nDigite sua opção (1/2/3/4/5): ")
if escolha =='1':
	print('Soma')
if escolha == '2':
	print('Subtração')
if escolha == '3':
	print('Multiplicação')
if escolha == '4':
	print('Divisão')
if escolha == '5':
	print('Porcentagem')
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == '1':
	print("\n'O resultado da soma é:")
	print(add(num1, num2))
	print("\n")

elif escolha == '2':
	print("\nO resultado da subtração é:")
	print(subtract(num1, num2))
	print("\n")

elif escolha == '3':
	print("\nO resultado da multiplicação é:")
	print(multiply(num1, num2))


elif escolha == '4':
	print("\nO resultado da divisão é:")
	print(divide(num1, num2))
	print("\n")

elif escolha == '5':
	print("\nO Resultado da porcentagem é:")
	print(percentage(num1, num2))
else:
	print("\nOpção Inválida!")