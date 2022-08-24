# O programa executa uma calculadora simples

# Esta função adiciona dois números
def add(x, y):
    return x + y


# Esta função subtrai dois números
def subtract(x, y):
    return x - y


# Esta função multiplca dois números
def multiply(x, y):
    return x * y


# Esta função divide dois números
def divide(x, y):
    return x / y


print('Selecione a operação:')
print('1. Somar')
print('2. Subtrair')
print('3. Multiplicar')
print('4. Dividir')

while True:
    # Receba a opção do usuário
    choice = input('Selecione uma opção (1/2/3/4): ')

    # Verifique se alguma das alternativas apresentadas foi escolhida
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))

        if choice == '1':
            print(f'{num1} + {num2} =', add(num1, num2))
        elif choice == '2':
            print(f'{num1} - {num2} =', subtract(num1, num2))
        elif choice == '3':
            print(f'{num1} * {num2} =', multiply(num1, num2))
        elif choice == '4':
            print(f'{num1} / {num2} =', divide(num1, num2))
        break
    else:
        print('Opção incorreta.')
