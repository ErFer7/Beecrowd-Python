# -*- coding: utf-8 -*-

# NOTA: Não pensei em uma implementação que não usasse vetores. Porém tenteni minimizar o seu uso para se manter
# no conteúdo.

# O código funciona da seguinte maneira: O problema pede que seja exibida uma linha com a palavra "Teste" e o
# número do teste, neste caso foi usada a variável count para contar os testes, em toda iteração do loop while
# o valor de count é incrementado.

# O loop while processa cada caso de teste e só é parado quando n e m são 0.

# A segunda etapa se trata de computar a menor e a maior média móvel entre as temperaturas na superfície da Lua.
# A ideia foi desenvolvida a partir do seguinte conceito: Dada uma lista [a, b, c, d] e o intervalo da média é
# possível criar um loop que calcule a média móvel. Cada iteração deste loop calcula uma média, no caso da lista
# descrita [a, b, c, d] as médias com intervalo 2 seriam: (a + b) / 2, (b + c) / 2 e (c + d) / 2. Para determinar
# o tamanho do loop pode-se pensar que é nessário que o loop chegue a calcular até a última média. Usando o mesmo
# exemplo anterior o comprimento da lista é 4 e o intervalo é 2, sendo assim a variável i do loop processando cada
# média chega até o item c, pois neste ponto do loop c e d serão calculados. Caso a lista tivesse o comprimento 7 e
# o intervalo fosse 4 o item máximo a ser atingido seria o quarto item. Com isso percebe-se o padrão 
# (Quantidade de iterações do loop = comprimento da lista - (intervalo - 1)).

# A próxima etapa é calcular a média dado os valores no intervalo do loop. Para isso existe um loop menor na linha
# 48 que faz a operação de calculo da média. O índice inserido na lista é a soma de j e i, o motivo disso é que a
# cada cálculo da média o i é incrementado, assim os valores do próximo intervalo são acessados.

# Por fim a comparação é feita com a média em relação aos registros de maior e menor média. Os valores da maior média
# e menor média (tMMax e tMMin) são declarados com valores que serão obrigatoriamente substituidos na primeira
# comparação.

# Depois de realizado o processamento os valores são exibidos.

# Variável para a contagem.
count = 0

# Loop que processa cada caso de testes.
while True:

    # Incrementa o contador em 1.
    count += 1

    # Vetor (lista) que irá conter as temperaturas.
    tLst = []

    # Variáveis para as médias mínimas e máximas, declaradas com valores que serão substituidos na primeira comparação
    tMMin = 250.0
    tMMax = -250.0

    # Input de n e m. O input é separado em um vetor de 2 elementos, esse vetor é mapeado com a função map()
    # aplicando a função int() nos 2 elementos, depois o mapa é convertido em uma lista.
    nm = list(map(int, input().split()))

    # Condição de saída, quebra o loop caso n e m sejam 0.
    if nm[0] == 0 and nm[1] == 0:
        break

    # Loop que processa cada input de temperatura.
    for i in range(nm[0]):

        # Armazena o input de uma temperatura como float.
        t = float(input())

        # Adiciona a temperatura na lista.
        tLst.append(t)
    
    # Loop que processa cada média.
    for i in range(nm[0] - (nm[1] - 1)):

        # Variável de média da temperatura.
        mT = 0.0

        # Loop que processa cada elemento da média.
        for j in range(nm[1]):

            # a média neste caso é dada pela reformulação da fórmula da média. Exemplo: (a + b) / 2 = a / 2 + b / 2. 
            # Então os valores são calculados individualmente e somados a variável da média.
            mT += tLst[j + i] / float(nm[1])

        # Compara a média com a maior média registrada.
        if mT > tMMax:

            # Substitui a maior média registrada caso a nova média seja maior.
            tMMax = mT
        
        # Compara a média com a menor média registrada.
        if mT < tMMin:

            # Substitui a menor média registrada caso a nova média seja menor.
            tMMin = mT
    
    # Escreve no console "Teste n".
    print("Teste {0}".format(count))
    # Escreve no console a menor e maior média truncada. (Neste caso convertida para int).
    print("{0} {1}\n".format(int(tMMin), int(tMMax)))