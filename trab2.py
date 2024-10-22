#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

#tarefa 1

#grafo do jogo

#cada casa do tabuleiro é um nó e as arestas são as casas vizinhas
Grafo = {
    1 : [2,4],
    2 : [1,3,5],
    3 : [2,6],
    4 : [1,5,7],
    5 : [2,4,6,8],
    6 : [3,5,9],
    7 : [4,8],
    8 : [5,7,9],
    9 : [6,8]
}

#grafo de estados do jooj
"""
Nesse grafo temos: 1) um n´o para cada configura¸c˜ao poss´ıvel do tabuleiro; 2) arestas
do tipo (cfg1, cfg2) quando pudermos passar da configura¸c˜ao cfg1 para a configura¸c˜ao cfg2 em um
s´o movimento do jogo.

"""

GrafoJogo = {
    
}

#tarefa 2
def BFS(G,s):  

    L = []
    L.append([s])
    visitados = []
    visitados[s] = 1
    parent = []
   
    i = 1

    while 1 :
        L.append([])
       
        for u in L[i-1]:
           
            for v in adj[u]:

                if(visitados[v] == 0):
                    L[i].append(v)
                    parent[v] = u
                    visitados[v] = 1

        if(len(L[i]) == 0):
            return

    return L

def BFS(G):
    visitados=[]
    componentes = 0
    for i in len(G):
        if(visitados[i] == 0):
            BFS(G,i)
            componentes += 1
    return componentes
   

#tarefa 3

def BFS(G,s):  

    L = []
    L.append([s])
    visitados = []
    visitados[s] = 1
    parent = []
   
    i = 1

    while 1 :
        L.append([])
       
        for u in L[i-1]:
           
            for v in adj[u]:

                if(visitados[v] == 0):
                    L[i].append(v)
                    parent[v] = u
                    visitados[v] = 1

        if(len(L[i]) == 0):
            return

    return parent

def BFS(G):
    visitados=[]
    for i in len(G):
        if(visitados[i] == 0):
            BFS(G,i)


# aqui tem q printar o parent