
preco_produto = float(input('Digite o valor do produto: R$'))

desconto_vista = .1
juros_prazo = .08

preco_vista = preco_produto - (preco_produto * desconto_vista)
preco_prazo = preco_produto + (preco_produto * juros_prazo)

print(f'Preço à vista = {preco_vista:.2f}\nPreço a prazo = R${preco_prazo:.2f}')