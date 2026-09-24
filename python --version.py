# Coletando os dados
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mes: '))
ano = int(input('Informe o ano: '))

# Verificando as condições
if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (ano > 0):
    print('Data válida')
else:
    print('Data inválida')

# Resultado
print(f'Dia: {dia}')
print(f'Mês: {mes}')
print(f'Ano: {ano}')