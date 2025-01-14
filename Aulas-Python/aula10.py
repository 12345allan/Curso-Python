# Formatação de Strings com o metodo format :   
# Tudo em python é um objeto, geralmente objetos tem métodos dentro deles;
# Objetos tem ações eles podem fazer algo;
# Metodos são funcões que podem fazer algo dentro do dado do objeto.
a = 'A'
b = 'B'
c = 1.1
string = 'a={nome_1} b={nome_2} c={nome_3:.2f}'
formato = string.format(
    nome_1=a, nome_2=b, nome_3=c)

print(formato)