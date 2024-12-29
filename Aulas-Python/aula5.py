# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) # Convertendo uma string para um inteiro usando o int dentro de uma classe e passando o int para o type para ver que foi convertido.
print(int('1') + 1) # Essa linha faz a soma de um str e um inteiro so que o str foi convertido para inteiro e no final a soma e feita por dois inteiros.
print(type(float('1') + 1))# Essa linha faz a conversão de um str para um float so que somando mais um e no final mostando o tipo.
print(bool(''))# Uma str vazia é considerada False.
print(bool(' '))# Uma str com algum valor ou até com espaço e considerada True.
print(str(11) + 'b')# Convertendo o número inteiro para str.