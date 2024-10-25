#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

from collections import defaultdict
from random import randint

#tarefa 1

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

def escolheTroca(posicaoVazia):
    # Seleciona aleatoriamente uma posição válida a partir dos movimentos possíveis
    # Define os movimentos válidos como deslocamentos (direita, esquerda, cima, baixo)
    return movimentos_validos[posicaoVazia][randint(0, len(movimentos_validos[posicaoVazia]) - 1)]
    
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
        key = next((chave for chave, valor in posicao.items() if valor == 0), None)
        valor = escolheTroca(key)
        
        posicaoVazia = posicao[valor]
        posicao[key] = posicaoVazia
        posicao[valor] = 0
        
        #verificar se o jogo acabou
        
        if posicao == configuracaoFinal:
            venceu = True
        
        
        #adicionar o estado do jogo no grafo
        #verificar se o estado ja existe no grafo
        if posicao not in GrafoJogo.values():
            GrafoJogo[cont] = posicao
            cont += 1
        
    
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