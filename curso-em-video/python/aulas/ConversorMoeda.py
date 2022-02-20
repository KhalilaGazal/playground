print('Conversor de moedas')

usd_exchange = float(input('Digite a cotação do dólar americano: R$'))
brl = float(input('Digite o valor em reais: R$'))

conversion_usd = brl / usd_exchange

print(f'R${brl:.2f} = US${conversion_usd:.2f}')
