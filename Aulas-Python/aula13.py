# Laços de repetição muda o fluxo do código
# elif e else depende do if
# O if não depende de ninguem 
# if  / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para a condição 1')
elif condicao2:
    print('Código para a condição 2')
elif condicao3:
    print('Código para a condição 3')
elif condicao4:
    print('Código para a condição 4')
else:
    print('Nenhuma condição foi satisfeita')
if 10 == 10:
    print('outro if')


print('Fora do if')