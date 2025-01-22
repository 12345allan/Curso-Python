# Operadores Lógicos 
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a qalquer expressão como verdadeiro,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é 
# usado para representar um não valor
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if condição: O if será executado se a expressão inteira for True
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""
# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha) 