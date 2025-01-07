# Precedência entre os operadores aritmétricos.
# Oque e precedências de operadores: A precedencia e quando uns operadores serão executados primeiros e depois outros.
# Se os operadores tiverem a mesma precedẽncia estiverem na mesma conta será executado da esquerda para a direita.
# 1. (n + n) - Parenteses: Primeiros a serem executados e são executados de dentro para fora.
# 2. ** - Potenciação: Segundo a ser excutado.
# 3. * / // % - Multiplicação, Divisão, Divisão inteira e Módulo: Terceiro a ser executado.
# 4. + - - Adição e Subtração: Quarto a ser executado.
conta_1 = (1 + 1) ** (5 + 5) # 1024
conta_1 = 'Qualquer coisa' # Trocando o valor da variável
conta_1 = (1 + int(0.5 + 0.5)) ** ( 5 + 5) # Essa linha mostra a conta sendo feita usando os parenteses internos a serem executados primeiro, int(0.5 + 0.5) convertendo um float para um inteiro 

print(conta_1)  