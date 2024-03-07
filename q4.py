# 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

import random
def verificar_interruptores(int1=False, int2=False, int3=False):
    tf = [True, False]
    sala = random.choices(tf, k=3)
    
    if int1 and int2:
        if not sala[0]:
            print('Interruptor 3 ligará a luz da sala A')
            int2 = False
            if sala[1]:
                print('Interruptor 1 liga a luz da sala B')
                print('e o Interruptor 2 liga a luz sala C')
            else:
                print('Interruptor 2 liga a luz da sala B')
                print('e o Interruptor 1 liga a luz sala C')
        else:
            if not sala[1]:
                int2 = False
                int3 = True
                print('O interruptor 2 liga a luz da sala B')
                print('O interruptor 1 liga a luz da sala A')
                print('logo o interruptor 3 liga a luz da sala C')
            else:
                if int1 and sala[0]:
                    print('O interruptor 1 liga a luz da sala A')
                    print('O interruptor 2 liga a luz da sala C')
                    print('logo o interruptor 3 liga a luz da sala B')
                elif int1 and sala[1]:
                    print('O interruptor 1 liga a luz da sala B')
                    print('O interruptor 3 liga a luz da sala C')
                    print('logo o interruptor 2 liga a luz da sala A')
    else:
        if sala[0] or sala[1]:
            print('Interruptor 1 ou Interruptor 2 ligam a luz da sala A')
            print('Volto desligo o Interruptor 2, ligo o Interruptor 3 e vou para sala B')
            if not sala[1]:
                print('O interruptor 2 liga a luz da sala B')
                print('O interruptor 1 liga a luz da sala A')
                print('logo o interruptor 3 liga a luz da sala C')
            else:
                print('O interruptor 1 poderá ligar a luz da sala A ou sala B')
                print('O interruptor 2 poderá ligar a luz da sala A ou sala C')
                print('O interruptor 3 poderá ligar a luz da sala B ou sala C')
                if sala[0]:
                    print('O interruptor 2 só poderá ligar a sala C')
                    print('logo o interruptor 3 ligará a sala B')
                else:
                    print('O interruptor 3 só poderá ligar a sala C')
                    print('logo o interruptor 2 ligará a sala A')

verificar_interruptores(True, True, False)

# Interruptor 1
# Interruptor 2
# Interruptor 3
# Sala A
# Sala B
# Sala C

# Ligo o Interruptor 1 e 2 e vou para a sala A
#     caso a luz esteja desligada:
#         o Interruptor 3 ligará a luz da sala A
#         Volto e desligo o Interruptor 2 e vou para a sala B
#             caso a luz esteja ligada:
#                 o Interruptor 1 liga a luz da sala B
#                 e o Interruptor 2 liga a sala C
#             caso a luz esteja desligado:
#                 o Interruptor 2 liga a sala B
#                 e o Interruptor 1 liga a sala C
#     caso a luz esteja ligada:
#         o Interruptor 1 ou Interruptor 2 ligam a luz da sala A
#         Volto desligo o Interruptor 2, ligo o Interruptor 3 e vou para sala B
#             caso a luz esteja desligada:
#                 o Interruptor 2 liga a luz da sala B
#                 o Interruptor 1 liga a luz da sala A 
#                 logo o Interruptor 3 liga a luz da sala C 
#             caso a luz esteja ligada:
#                 O Interruptor 1 poderá ligar a luz da [sala A ou sala B]
#                 O Interruptor 2 poderá ligar a luz da [sala A ou sala C]
#                 O Interruptor 3 poderá ligar a luz da [sala B ou sala C]
#                     caso o Interruptor 1 ligue a sala A
#                         o Interruptor 2 só poderá ligar a sala C
#                             logo o Interruptor 3 ligará a sala B
#                     caso o Interruptor 1 ligue a sala B
#                         o Interruptor 3 só poderá ligar a sala C 
#                             logo o Interruptor 2 ligará a sala A

