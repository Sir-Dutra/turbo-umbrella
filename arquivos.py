import shutil
'''
programa simples para ler, ecrever e tratar informações em arquivos externos
exemplo:escrever, ler e tirar a media de notas de alunos
'''


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))

def copia_arquivo(nome_arquivo):
   shutil.copy(nome_arquivo, 'C:/MeusDocumentos/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/MeusDocumentos/')



if __name__ == '__main__':
    media_notas('notas.txt')
    #escrever_arquivo('primeira linha.\n')
    #aluno = 'tiago, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')
    #copia_arquivo(notas.txt)
    #move_arquivo(notas.txt)
