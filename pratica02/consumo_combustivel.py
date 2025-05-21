"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

dist_percor = 300
combust = 25
consumo_medio = dist_percor / combust
arrendondar = round(consumo_medio, 2)

print(f"O consumo médio para uma distância percorrida de {dist_percor}km com um gasto de {combust} litros é {arrendondar:.2f}km/l")
