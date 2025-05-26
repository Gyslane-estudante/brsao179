"""
Crie outra operações e teste no executar_operacao
subtrair(x, y)
dividir(x,y)
ao_quadrado_da_soma(x, y) -> retorna (x+y) ** 2
"""

x = int(input("\nInforme o primeiro número: "))
y = int(input("\nInforme o segundo número: "))


def soma(x, y):
    return x + y

def mult(x, y):
    return x * y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def square_sum(a ,b):
    return (x + y) ** 2

def execute_op(x, y, func):
    return func(x, y)


print(f"O resultado da soma é: {execute_op(x, y, soma)}")
print(f"O resultado da multiplicação é: {execute_op(x, y, mult)}")
print(f"O resultado da subtração é: {execute_op(x, y, sub)}")
print(f"O resultado da divisão é: {execute_op(x, y, div)}")
print(f"O resultado do quadrado da soma é: {execute_op(x, y, square_sum)}")


