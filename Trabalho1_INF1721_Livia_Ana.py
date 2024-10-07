#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

import random
import time
import matplotlib.pyplot as plt

#Tarefa 1

def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


def LinearSelection(A, k):
    
    #Caso base da recursao
    if(len(A) == 1):
        return A[0]
    
    #Caso k esteja fora dos limites (i.e., ≤ 0 ou > |A|), retorne mensagem de erro/excecucao
    if(k <= 0 or k > len(A)):
        return "Erro: k fora dos limites"
    
    #array de arrays 
    arr = [] 
    #array de medianas                      
    M = []   
                           
    #Divide A em grupos de 5 elementos cada
    for i in range(0, len(A), 5): 
        arr.append(A[i:i+5])
    
    for i in range(len(arr)): 
        #Ordena cada grupo de 5 elementos
        InsertionSort(arr[i]) 
        #Adiciona a mediana de cada grupo ao array M
        M.append(arr[i][len(arr[i])//2]) 
    
    #Encontre a mediana m’ de M recursivamente
    
    mediana = LinearSelection(M, len(M)//2) 
    
    #Particiona A em 3 subconjuntos L, R e E

    L = []
    R = []
    E = []
    
    #Adiciona os elementos de A em L, R ou E
    for i in range(len(A)):
        if A[i] < mediana:
            L.append(A[i])
        elif A[i] > mediana:
            R.append(A[i])
        else:
            E.append(A[i])
    
    #Se |L| = k-1, retorne m’
    if(len(L) == (k - 1)):
        return mediana
    
    #Se |L| ≥ k, retorne LinearSelection(L, k)
    elif(len(L) >= k):
        return LinearSelection(L, k) 
    
    #Se k ≤ |L| + |E|, retorne m’
    elif len(L) + len(E) >= k:
        return mediana
    
    #Se |L| + |E| < k, retorne LinearSelection(R, k-|L|-|E|)
    else:
        return LinearSelection(R, k - len(L) - len(E)) 
    

#Teste de array sem numeros repetidos e tamanho multiplo de 5 
A = [3,6,8,9,2,7,1,4,0,5]
print("Teste1 :",LinearSelection(A, 4))

#Teste de array sem numeros repetidos e tamanho nao multiplo de 5 
An = [3,6,8,9,2,7,1,4,0]
print("Teste 2 : ",LinearSelection(An, 4))

#Teste de array com numeros repetidos e tamanho multiplo de 5  
Ar = [3,6,5,9,2,7,1,4,0,5]
print("Teste 3 : ",LinearSelection(Ar, 4))

#Teste de array com todos os numeros iguais 
Aigual = [3,3,3,3,3,3,3,3,3,3]
print("Teste 4 : ",LinearSelection(Aigual, 4))

#Teste de array com numeros repetidos e tamanho nao multiplo de 5
Arn = [3,6,5,9,2,7,1,4,5]
print("Teste 5 : ",LinearSelection(Arn, 4))

#Teste com k fora dos limites
A1 = [1,2]
print("Teste 6 : ",LinearSelection(A1, 4))

#Teste com array de tamaho 1
print("Teste 7 : ",LinearSelection(A1, 1))


#Tarefa 2

def BubbleSort(A):
    for i  in range (0,len(A)) :
        for j  in range(1,len(A)-i):       
            if A[j-1] > A[j]:
                #swap
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
    return A


def SortSelection(A, k):
    Aord = BubbleSort(A)
    return Aord[k-1] 

#Arrays pra armazenar os tempos de execucao
arr_medias_sort = []
arr_medias_linear = []

#Variaveis para contar o tempo de execucao
tempoSort = 0
tempoLinear = 0

#Para cada n = 1.000, 2.000, . . . , 10.000
for n in range(1000, 11000, 1000):
    #gere 10 instancias aleatorias de tamanho n (total de 100 instancias)
    for i in range(10):
        
        Sort = []
        
        Linear = []
        
        for j in range(n):
            #Os numeros em cada instancia devem ser gerados aleatoriamente entre 1 e 100.000
            r = random.randint(1, 100000)
            
            Sort.append(r)
            
            Linear.append(r)
        
        #Sempre k = ⌊n/2⌋ (metade do tamanho da lista de entrada arredondada para baixo)
        k = len(Sort)//2
        
        #Comeca a contar o tempo de execucao do SortSelection
        time1 = time.time()
        
        #Executa o SortSelection e imprime o resultado
        print("SortSelection = ",SortSelection(Sort, k))
        
        time2 = time.time() - time1
        
        #Soma o tempo de execucao do SortSelection para calcular a media
        tempoSort += time2
        
        #Comeca a contar o tempo de execucao do LinearSelection
        time3 = time.time()
        
        #Executa o LinearSelection e imprime o resultado
        print("LinearSelection = ",LinearSelection(Linear, k))
        
        time4 = time.time() - time3
        
        #Soma o tempo de execucao do LinearSelection para calcular a media
        tempoLinear += time4
    
    #Calcula a media dos tempos de execucao
    arr_medias_sort.append(tempoSort/10)
    arr_medias_linear.append(tempoLinear/10)
        

#Tamnhos das entradas
x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

#Médias dos tempos de execução
y1 = arr_medias_sort
y2 = arr_medias_linear

# Série 1
plt.plot(x, y1, label="SortSelection", color='blue', marker='o')  

# Série 2
plt.plot(x, y2, label="LinearSelection", color='green', marker='x')    

# Adicionar título e legendas
plt.title("Gráfico dos Tempos de Execução por Tamanho da Entrada")
plt.xlabel("Tamanho da Entrada")
plt.ylabel("Média dos Tempos de Execução")

# Adicionar a legenda
plt.legend()

# Mostrar o gráfico
plt.show()
