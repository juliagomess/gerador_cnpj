import cnpj

#while True:
print()
cnpj1 = input('Digite seu CNPJ: ')

if cnpj.valida_entrada(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')

gerador=cnpj.gera()
formatado=cnpj.formata(gerador)
print(formatado)

#valida = input('Deseja colocar mai CNPJ (s/n)? ')
#if valida == 'n':
#    break