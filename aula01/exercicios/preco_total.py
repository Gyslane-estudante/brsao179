nome_produto = 'Cadeira Infantil'
preco = 12.40
qtd = 3

total = preco * qtd
total_format = f'{total:.2f}'
print(f'\nO valor total da compra de {qtd} unidades do produto {nome_produto} é R$ {total_format}')