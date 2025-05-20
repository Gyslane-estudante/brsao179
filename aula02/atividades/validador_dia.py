#Quero saber se o dia é útil ou não

dia = (input("Digite o dia da semana: "))
if dia == "Sábado" or dia == "Domingo":
    print("Fim de semana")
else:
    print(f"O dia {dia} é um dia útil")