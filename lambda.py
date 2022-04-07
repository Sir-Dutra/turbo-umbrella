contador_letras = lambda lista: [len(x) for x in lista]

lista_teste = ['dale', 'dele', 'doeel']
print(contador_letras(lista_teste))

#soma = lambda a, b: a + b

#print(soma(5, 5))

calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a,b: a-b,
    'multi': lambda a,b: a*b,
    'div': lambda a,b: a/b,
}

print(type(calculadora))

soma = calculadora['soma']
print(soma(1, 5))