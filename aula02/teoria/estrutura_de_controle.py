"""
Se está chovendo:
        levo o guarda-chuva
    senão:
        está ensolarado e passo o protetor solar
    senão:
        estou de boa na lagoa
"""

true_chovendo = False
true_ensolarado = True
cor_guarda_chuva = "Preto"

def levar_guarda_chuva(cor):
    print(f"Está chovendo. Levo o meu guarda-chuva {cor}.")

def passo_protetor():
    print("Está ensolarado e estou passando o protetor solar")

def estou_de_boa():
    print("O tempo está de boa")

if true_chovendo:
    levar_guarda_chuva(cor_guarda_chuva)
elif true_ensolarado:
    passo_protetor()
else:
    estou_de_boa()