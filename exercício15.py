km = float(input('Digite quantos km você percorreu: '))
dias = float(input('Digite quantos dias você ficou com o carro alugado: '))
valor = (km * 0.15) + (dias * 60)
print('O valor total a ser pago é R$ {:.2f}'.format(valor))