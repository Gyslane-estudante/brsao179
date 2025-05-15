preco = 1000
desconto = 15

valor_final = preco - (preco * desconto / 100)
valor_format = f'{valor_final:.2f}'
print(f"\nO preço do celular de Maria com {desconto}% de desconto é R$ \033[1m{valor_format}\033[0m")