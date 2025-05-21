"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_orig = 50.00
desc = 20
preco_desc = preco_orig * (desc / 100)

print(f"O valor do produto {nome_produto} que tem o valor normal de R${preco_orig:.2f} recebeu um desconto de {desc}%. Diante disso o nome valor é R${preco_desc:.2f}")