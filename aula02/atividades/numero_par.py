#Quero saber se o número é par

num = int(input("Digite um número: "))

if not (num % 2 == 0):
    print(f"Ímpar")
else:
    print(f"Par")