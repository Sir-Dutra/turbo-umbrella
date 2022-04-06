class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b
try:
    x = int(input('numero um: '))
    imp = (input('tipo de operação: '))
    y = int(input('numero 2: '))
except:
    print("não foi inserido um numero valido")


calculadora = Calculadora()
if (imp =='+'):
    print (f'o resultado da soma é: {calculadora.soma(x, y)}')
elif (imp=='-'):
    print(f'o resultado da subitração é: {calculadora.subtracao(x, y)}')
elif (imp=='*'):
    print(f'o resultado da multiplicação é: {calculadora.multiplicacao(x, y)}')
elif (imp=='/'):
    print(f'o resultado da divisão é {calculadora.divisao(x, y)}')
else:
    print(f'operação invalida')


