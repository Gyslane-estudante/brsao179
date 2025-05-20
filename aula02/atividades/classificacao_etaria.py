#Quero saber se a pessoa é idosa, adulta, adolescente, criança ou bebê

idade = int(input("Digite a sua idade: "))

if idade >= 65:
    print(f"idoso")
elif idade >= 18:
    print(f"Adulto")
elif idade >= 12:
    print(f"Adolescente")
elif idade >= 3:
    print(f"Criança")
else:
    print(f"Bebê")