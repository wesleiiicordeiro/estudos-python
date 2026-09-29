#ativdade 11
#dicionário com suas respectivas chaves e valores
dicionario_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
# um laço for para selecionar todos os valores
for valores in dicionario_vendas.values():
  # variavel total_vendas com o operador que serve para somar e guardar valores
  total_vendas += valores
print(f'O total das vendas são: {total_vendas}')
# utilizei a função max para selecionar o dicionario e a as chaves
#(.get) serve para mostrar para o  programa que quero mostrar os valores(os numeros)
mais_vendido = max(dicionario_vendas, key=dicionario_vendas.get)
print(f'O produto mais vendido foi: {mais_vendido}')

#atividade 12
#dados do dicionario
dicionario_votos_marca ={ 
'Design 1': 1334,
'Design 2': 982,
'Design 3': 1751,
'Design 4': 210,
'Design 5' : 1811}
#uma variavel para receber a funcao max para demostrar a chave de maior valor
mais_votado = max(dicionario_votos_marca,key=dicionario_votos_marca.get)
# uma varaivel para receber o mais votado e mostar a quantidade de votos 
votos_vencedor = dicionario_votos_marca[mais_votado]
print(f'O design mais votado foi o {mais_votado} com {votos_vencedor} votos.')
