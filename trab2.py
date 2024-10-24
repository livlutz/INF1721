#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

#tarefa 1

#grafo do jogo

Grafo = {
    
}

#grafo de estados do jooj
"""
Nesse grafo temos: 1) um n´o para cada configura¸c˜ao poss´ıvel do tabuleiro; 2) arestas
do tipo (cfg1, cfg2) quando pudermos passar da configura¸c˜ao cfg1 para a configura¸c˜ao cfg2 em um
s´o movimento do jogo.

"""

#configuracao final : 1 2 3
#                     4 5 6
#                     7 8 


def montaGrafoEstados():
    
    
    
    
    return GrafoJogo

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

   
print("O número componentes conexas = ", BFS(GrafoJogo))

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

    
    return len(L)

def BFS(G):
    visitados=[]
    maxCaminho = -1
    for i in len(G):
        if(visitados[i] == 0):
            tamCaminho = BFS(G,i)
        if(tamCaminho > maxCaminho):
            maxCaminho = tamCaminho
    return maxCaminho

print("Maior caminho mais curto = ", BFS(GrafoJogo))