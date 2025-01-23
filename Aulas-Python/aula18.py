# Operadores in e not in
# in = Retorna True se o elemento for encontrado na sequência e retorna False se o elemento não está presente na sequência. 
# not in = Retorna True se o elemento não for encontrado na sequência e retorna False quando o elemento e encontrado na sequência.
# Strings em Python são interáveis (Posso navegar item por item) 
# 0 1 2 3 4 5
# A l l a n r
# -6-5-4-3-2-1
#nome = 'Allan'
#print(nome[2])
#print(nome[-4])
#print('lan' in nome)
#print('zero' in nome)
#print(10 * '-')
#print('lan' not in nome)
#print('zero' not in nome)

nome = input('Digite se nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')