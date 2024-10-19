#tarefa 1

#Aparentemente, hash table em python é dicionário

#grafo do jogo
G = {

    1 :
    2 :
    3 :
    4 :
    5 :
    6 :
    7 :
    8 :

}

#grafo de estados do jooj
"""
Nesse grafo temos: 1) um n´o para cada configura¸c˜ao poss´ıvel do tabuleiro; 2) arestas
do tipo (cfg1, cfg2) quando pudermos passar da configura¸c˜ao cfg1 para a configura¸c˜ao cfg2 em um
s´o movimento do jogo.

"""


GrafoE = {
    #n sei se tá certo mas é a configuração final
    cfgfinal : (G[1],G[2],G[3],G[4],G[5],G[6],G[7],G[8])
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