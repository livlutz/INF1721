#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

from collections import defaultdict
from random import randint

#tarefa 1

"""#tirar os estados repetidos
     # Remove duplicados após a geração de todos os estados
    estados_unicos = {tuple(state.values()): state for state in GrafoJogo.values()}
    
    # Converte o grafo para usar apenas os estados únicos
    GrafoJogoUnico = {i + 1: estado for i, estado in enumerate(estados_unicos.values())}"""

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
def geraTrocas(posicao, key):
    trocas = []
    for destino in movimentos_validos[key]:
        nova_posicao = posicao.copy()
        nova_posicao[key], nova_posicao[destino] = nova_posicao[destino], nova_posicao[key]
        trocas.append(nova_posicao)
    return trocas
    
def montaGrafoEstados(posicoesIniciais):
    
    posicao = posicoesIniciais.copy()
    
    GrafoJogo = {
        1 : posicao.copy(),
    }
    
    venceu = False
    cont = 2
    
    while not venceu :
        #alterar o estado do jogo, ver onde ta o 0 e trocar com qqlr posicao vizinha
        #lado = posicao.index(0) +-1
        #cima e baixo = posicao.index(0) +-3
    
        posicao_atual = GrafoJogo[cont - 1].copy()
        key_vazio = next((k for k, v in posicao_atual.items() if v == 0), None)
        trocas_possiveis = geraTrocas(posicao_atual, key_vazio)
        
        for nova_posicao in trocas_possiveis:
            if nova_posicao not in GrafoJogo.values():
                GrafoJogo[cont] = nova_posicao
                cont += 1
                # Verifica se venceu
                if nova_posicao == configuracaoFinal:
                    venceu = True
                    break
        
    return GrafoJogo
    
   
GrafoJogo = montaGrafoEstados(posicoesIniciais)
print(len(GrafoJogo))

#tarefa 2
"""
def BFS(G,s):  

    L = []
    L.append([s])
    visitados = defaultdict(lambda: 0)
    visitados[s] = 1
   
    i = 1

    while 1 :
        L.append([])
       
        for u in L[i-1]:
           
            for v in G[u]:

                if(visitados[v] == 0):
                    L[i].append(v)
                    visitados[v] = 1

        if(len(L[i]) == 0):
            break
        
        i += 1

    return L

def BFS(G):
    visitados = defaultdict(lambda: 0)
    componentes = 0
    for i in len(G):
        if(visitados[i] == 0):
            BFS(G,i)
            componentes += 1
    return componentes

   
print("O número componentes conexas = ", BFS(GrafoJogo))

#tarefa 3

def BFS(G,s):  

    L = []
    L.append([s])
    visitados = defaultdict(lambda: 0)
    visitados[s] = 1
   
    i = 1

    while 1 :
        L.append([])
       
        for u in L[i-1]:
           
            for v in G[u]:

                if(visitados[v] == 0):
                    L[i].append(v)
                    visitados[v] = 1
        
        if(len(L[i]) == 0):
            break
        
        i += 1

    
    return len(L)

def BFS(G):
    visitados = defaultdict(lambda: 0)
    maxCaminho = -1
    for i in len(G):
        if(visitados[i] == 0):
            tamCaminho = BFS(G,i)
        if(tamCaminho > maxCaminho):
            maxCaminho = tamCaminho
    return maxCaminho

print("Maior caminho mais curto = ", BFS(GrafoJogo)) """