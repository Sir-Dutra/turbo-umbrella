'''
testando as funcionalidades de try, except, else e finaly
'''

lista = [1, 10]
try:
    arquivo = open ('teste.txt', 'r')
    div = 10 / 0 #div = 10 / 0
    numero = lista[1] #numero = lista[5]
    print('fechando arquivo')# não foi fechado pelo erro na divisão
    arquivo.close()
    #x = x
except ZeroDivisionError:
    print('não é possivel dividir por zero')
except IndexError:
    print('erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print(f'erro descnhecido {ex}')
else:
    print(f'não houve nenhum erro')
finally:
    print('sempre executado')
    arquivo.close()