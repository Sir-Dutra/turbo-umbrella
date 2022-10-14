import random


def play():
    jogador = input(" qual a sua escolha? 'pe' para pedra, 'pa' para papel e 't' para tesoura\n")
    computador = random.choice (['pe', 'pa', 't'])
    print (f'o computador escolheu {computador}')

    # pe > t, t > pa, pa> pe
    if jogador == computador:
        return 'empate'

    if vitoria(jogador, computador):
        return 'Você ganhou'
    
    return 'Você perdeu'



def vitoria(usuario, oponente):
    #return true se o usuario ganhar
    # pe > t, t > pa, pa> pe

    if (usuario == 'pe' and oponente == 't') or (usuario == 't' and oponente == 'pa') or ( usuario == 'pa' and oponente == 'pe'):
        return True


print (play())
