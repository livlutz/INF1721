#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

from collections import defaultdict, deque
from random import randint

#Tarefa 1

# Gerando uma configuração inicial com posicoes aleatorias

numerosAleatorios = []
cont = 0

while cont < 9:
    num = randint(0,8)
    
    if num not in numerosAleatorios:
        numerosAleatorios.append(num)
        cont += 1
    
# 0 e a casa vazia
posicoesIniciais = {
    1 : numerosAleatorios[0],
    2 : numerosAleatorios[1],
    3 : numerosAleatorios[2],
    4 : numerosAleatorios[3],
    5 : numerosAleatorios[4],
    6 : numerosAleatorios[5],
    7 : numerosAleatorios[6],
    8 : numerosAleatorios[7],
    9 : numerosAleatorios[8]
}

# Configuração final que queremos atingir para completar o puzzle
configuracaoFinal = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 0
}

# Possíveis trocas que podem ser feitas a partir de cada posição
movimentos_validos = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8],
    8: [5, 7, 9],
    9: [6, 8]
}

# Função para gerar todas as trocas a partir da posição vazia
def escolheTroca(posicaoVazia):
    return movimentos_validos[posicaoVazia][randint(0, len(movimentos_validos[posicaoVazia]) - 1)]
    
def montaGrafoEstados(posicoesIniciais):
    
    #H[cfg] retorna o numero do no relativo a essa configuracao
    H = {}
    
    #C[u] retorna a configuracao correspondente a esse no
    C = [] 
    
    GrafoJogo = {}

    posicao = posicoesIniciais.copy()
    posicao_tupla = tuple(posicao.values())  # Converte a configuração inicial em tupla para hashing

    H[posicao_tupla] = 0
    C.append(posicao.copy())
    GrafoJogo[0] = {"cfg": posicao.copy(), "viz": []}

    #Flags de controle do while
    venceu = False
    cont = 1
    
    while not venceu :
    
        #alterar o estado do jogo, ver onde ta o 0 e trocar com qqlr posicao vizinha
        #lado = posicao.index(0) +-1
        #cima e baixo = posicao.index(0) +-3

        posicao_atual = C[cont - 1]  # Aqui ainda é uma lista
        #print("Posicao atual = ", posicao_atual)

        key_vazio = key_vazio = next(k for k, v in posicao_atual.items() if v == 0)  # Encontra a chave (posição) onde o valor é 0 
        #print("Key vazio = ", key_vazio)

        nova_posicao_vazia = escolheTroca(key_vazio)
        
        posicao_atual[key_vazio] = posicao_atual[nova_posicao_vazia]
        posicao_atual[nova_posicao_vazia] = 0
        posicao_tupla = tuple(posicao_atual.values())

        H[posicao_tupla] = cont
        C.append(posicao_atual)
        GrafoJogo[cont] = {"cfg": posicao_tupla, "viz": [cont - 1]}
        GrafoJogo[cont - 1]["viz"].append(cont)
        cont += 1
            
        if posicao_atual == configuracaoFinal:
            venceu = True
            break
        
        
    return GrafoJogo
    
   
GrafoJogo = montaGrafoEstados(posicoesIniciais)

print("Quantidade de estados = ", len(GrafoJogo), "\n")
print("Quantidade de arestas = ", sum([len(GrafoJogo[i]["viz"]) for i in GrafoJogo])//2, "\n")

#Tarefa 2

def BFS_visit(G, s, visitados):
    listaNos = deque([s])
    visitados[s] = True

    while listaNos:
        u = listaNos.popleft()
        for v in G[u]["viz"]:
            if not visitados[v]:
                listaNos.append(v)
                visitados[v] = True

def BFS(G):
    visitados = defaultdict(lambda: 0)
    componentes = 0
    for i in G:
        if(visitados[i] == 0):
            BFS_visit(G,i, visitados)
            componentes += 1
    return componentes

print("O número componentes conexas = ", BFS(GrafoJogo))

#Tarefa 3

def BFS_visit_caminho(G, s, visitados):  
    listaNos = deque([(s, 0)])  
    visitados[s] = True
    max_caminho = 0

    while listaNos:
        u, dist = listaNos.popleft()  
        max_caminho = max(max_caminho, dist) 

        for v in G[u]["viz"]:
            if not visitados[v]:
                listaNos.append((v, dist + 1))
                visitados[v] = True

    return max_caminho

def BFS_caminho(G):
    visitados = defaultdict(lambda: False)
    max_caminho = -1

    for i in G:
        if not visitados[i]:  
            tam_caminho = BFS_visit_caminho(G, i, visitados)
            max_caminho = max(max_caminho, tam_caminho)

    return max_caminho

print("Maior caminho mais curto =", BFS_caminho(GrafoJogo))