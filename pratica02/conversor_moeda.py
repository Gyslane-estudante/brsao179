"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

moeda_real = 100.00
tx_dolar = 5.20
tx_euro = 6.15
convert_dolar = moeda_real / tx_dolar
convert_euro = moeda_real / tx_euro

print(f"\nO valor do real R${moeda_real:.2f} convertido para dólar é US${convert_dolar:.2f}")
print(f"O valor do real R${moeda_real:.2f} convertido para euro é €{convert_euro:.2f}")