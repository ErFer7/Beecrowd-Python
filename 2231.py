# -*- coding: utf-8 -*-

# NOTA: Não pensei em uma implementação que não usasse vetores.

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

# A próxima etapa é calcular a média dado os valores e intervalo. Com a lista das temperaturas é possível
# implementar a média móvel. O intervalo que será somado pode ser extraido da lista com o corte da mesma
# Desta maneira é possível cortar a lista a partir do início do intervalo até o final. O início do intervalo será
# o índice i do loop, já que a cada iteração o i será incrementado em 1 aumentando o início do intervalo. O final
# do intervalo é dado por (intervalo + 1) porque o final do corte não é inclusivo o +1 considera o último elemento.
# Assim que os valores do intervalo é obtido é feito o somatório e a divisão pelo próprio intervalo, obtendo-se
# a média que é adicionada diretamente a lista de médias que será processada depois.

# Por fim a maior e menor média são calculadas com as funções min() e max() na lista de médias.

# Detalhe: para intervalos 1 a média é o próprio elemento em si, então não é necessário fazer cálculo da média
# móvel.

# Depois de realizado o processamento os valores são exibidos com suas devidas correções.

# Variável para a contagem.
count = 0

# Loop que processa cada caso de testes.
while True:

    # Incrementa o contador em 1.
    count += 1

    # Vetor (lista) que irá conter as temperaturas.
    tLst = []

    # Input de n e m. O input é separado em um vetor de 2 elementos e depois mapeado e convertido para int.
    n, m = map(int, input().split())

    # Condição de saída, quebra o loop caso n e m sejam 0.
    if n == 0 and m == 0:
        break

    # Loop que processa cada input de temperatura.
    for i in range(n):

        # Armazena o input de uma temperatura.
        t = input()

        # Adiciona a temperatura na lista.
        tLst.append(t)

    # Converte todas as temperaturas para float.
    tLst = list(map(float, tLst))

    # Lista de médias
    mTLst = []

    # Intervalo convertido para float.
    inter = float(m)

    # Variáveis da média mínima e máxima.
    mTMin = 0
    mTMax = 0

    # Se o intervalo é 1 a média é o próprio elemento, então as médias máximas e mínimas serão os elementos máximos
    # e mínimos. Caso contrário o calculo é realizado no bloco abaixo.
    if m != 1:

        # Loop que processa cada média.
        for i in range(n - (m - 1)):

            # Adiciona a média na lista como explicado no comentário principal.
            mTLst.append(sum(tLst[i: m + i]) / inter)
        
        # Obtem a média mínima e máxima.
        mTMin = min(mTLst)
        mTMax = max(mTLst)
    else:

        # Define a média mínima e máxima como a temperatura mínima e máxima.
        mTMin = min(tLst)
        mTMax = max(tLst)

    # Escreve no console "Teste n".
    print("Teste {0}".format(count))
    # Escreve no console a menor e maior média truncada. (Neste caso convertida para int).
    # Detalhe, os valores são arredondados na 12° casa decimal por causa dos erros de precisão que estavam
    # causando problemas na avaliação do URI.
    print("{0} {1}\n".format(int(round(mTMin, 12)), int(round(mTMax, 12))))