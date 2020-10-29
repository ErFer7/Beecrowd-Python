# -*- coding: utf-8 -*-

from math import ceil

# Considerando que a cada dia uma posição é preenchida a quantidade de dias teria que ser o tempo levado para
# preencher a maior distância entre os pontos iniciais. A maneira que estes pontos são preenchidos depende se a
# maior distância está entre dois pontos ou se está entre uma ponta da fita e um ponto. Além disso deve ser
# considerado se há apenas um ponto na fita.

# Para os casos em que há apenas um ponto as distâncias a serem consideradas são entre o início e o fim da fita.

# Para os casos em que há mais de um ponto as distâncias serão entre o início da fita, entre pontos e até o fim
# da fita.

# Quando a distância máxima é de um ponto até uma ponta da fita o número de dias será a própria distância, já que 7
# a cada dia um ponto é preenchido.

# Quando a distância máxima é de um ponto até outro ponto o número de dias será a metade da distância, porque cada
# ponto irá se expandir a cada dia, então com a expanção dos dois a distância entre os espaços preenchidos se reduz
# 2x por dia.

# Para resolver o problema é utilizada uma lista que contêm as distâncias, o primeiro e último elemento correspondem
# as distâncias do íncio a um ponto e do fim a um ponto respectivamente. Todas as outras distâncias são entre pontos.

# Variável para o resultado
res = 0

# Lista para as distâncias
d = []

# Input do tamanho da fita e a quantidade de pontos
f, r = map(int, input().split())

# Input das posições
rL = list(map(int, input().split()))

# Caso só exista um ponto
if r == 1:

    # Calcula a distância entre o início da fita e o ponto, depois registra na lista
    d.append(rL[0] - 1)

    # Calcula a distância entre o fim da fita e o ponto, depois registra na lista
    d.append(f - rL[0])
# Caso só existam mais de um ponto
else:

    # Loop para cada ponto
    for i in range(r):

        # Caso seja o primeiro ponto
        if i == 0:

            # Calcula a distância entre o início da fita e o ponto, depois registra na lista
            d.append(rL[i] - 1)
        # Caso seja um ponto intermediário
        elif i != r - 1:

            # Calcula a distância entre o ponto anterior e o ponto atual, depois registra na lista
            d.append(rL[i] - rL[i - 1] - 1)
        # Caso seja o último ponto
        else:

            # Calcula a distância entre o ponto anterior e o ponto atual, depois registra na lista
            d.append(rL[i] - rL[i - 1] - 1)

            # Calcula a distância entre o fim da fita e o ponto, depois registra na lista
            d.append(f - rL[i])

# Caso a maior distância seja entre uma das pontas da fita e o ponto
if max(d) == d[0] or max(d) == d[-1]:

    # Calcula o resultado
    res = max(d)
# Caso a maior distância seja entre dois pontos
else:

    # Calcula o resultado, o número é sempre arredondado para cima com a função "ceil()". Assim condições de 
    # divisões inexatas são consideradas
    res = ceil(max(d) / 2)

# Exibe o resultado
print(res)