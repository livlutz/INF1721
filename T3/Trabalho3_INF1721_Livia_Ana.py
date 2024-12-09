#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

#Para fins de teste, basta mudar o nome do arquivo usado e o path para o mesmo arquivo
arquivo = open(r"C:\Users\Livia\git\INF1721\T3\inst1.txt", "r")

#lendo o arquivo aberto
linha = arquivo.readline()

partes = linha.strip().split(" ")

#pegando o numero de itens e o tamanho da mochila
n = int(partes[0])
B = int(partes[1])

linha = arquivo.readline()

#Arrays para armazenar o tamanho e o valor de cada item
tam = []
valor = []

#Pegando o valor e o tamanho de cada item
while linha != "":
    partes = linha.strip().split(" ")

    valor.append(int(partes[0]))
    tam.append(int(partes[1]))

    linha = arquivo.readline()

arquivo.close()

#Inicializando o array de opt e o array de quantidade de itens
m = [[0 for _ in range(B+1)] for _ in range(n+1)]
qtdItens = [0 for _ in range(n+1)]  
      
def Knapsack(i,b,m,valor,tam,qtdItens):
    if ((i == 0) or (b == 0)):
        return 0
    
    maior = -1000000
    
    #Preenche o array usando a equacao de recorrencia OPT(i,b) = max (j = 1…10) { (j*vi) + OPT(i - 1,b - (j * vi)), OPT(i-1,b) }
    for n in range(1,i+1):
        for w in range(1,b+1):
            m[n][w] = m[n-1][w]
            for j in range(1,11):
                #Verifica o tamanho do item
                if j * tam[n-1] <= w:
                    m[n][w] = max(m[n][w], (j * valor[n-1]) + m[n-1][w - (j * tam[n-1])])
                    if m[n][w] > maior:
                        #Guarda o maior valor encontrado ate o momento
                        maior = m[n][w]
    
    #Preenche o array de quantidade de itens
    w = b
    for n in range(i, 0, -1):  
        for j in range(10, 0, -1):  
            #Verifica o tamanho do item e se é opt
            if ((j * tam[n-1]) <= w) and (m[n][w] == (j * valor[n-1]) + m[n-1][w - (j * tam[n-1])]):
                #Guarda a quantidade de itens usados 
                qtdItens[n] = j  
                #Atualiza o tamanho da mochila restante
                w -= (j * tam[n-1])  
                break
    
    #Retorna o maior valor encontrado e a quantidade de itens usados
    return maior, qtdItens
    
def imprimeResultado(maior,qtdItens,indArq):
    print("Melhor valor obtido na instancia ",indArq,": ", maior,"\n")
    for i in range(1,n+1):
        print("Foram usados ",qtdItens[i]," do item numero ", i,"\n")

maior,qtdItens = Knapsack(n,B,m,valor,tam,qtdItens)

#Para testar, basta mudar o ultimo parametro da funcao para o numero da instancia do arquivo sendo testado
imprimeResultado(maior,qtdItens,1)

        
