#Lívia Lutz dos Santos - 2211055
#Ana Luiza Pinto Marques - 2211960

#guardando os nomes dos arquivos pra ler

#nomeArquivo = "inst"
#arquivos = []
#for i in range (1,9):
    #arquivos.append(nomeArquivo + str(i) )


#primeira linha -> n itens e j capacidade da mochila
#as outras sao valor e tamanho

tam = []
valor = []

arquivo = open(r"C:\Users\Livia\git\INF1721\T3\inst1.txt", "r")
linha = arquivo.readline()

partes = linha.strip().split(" ")

n = int(partes[0])
B = int(partes[1])

linha = arquivo.readline()

while linha != "":
    partes = linha.strip().split(" ")

    valor.append(int(partes[0]))
    tam.append(int(partes[1]))

    linha = arquivo.readline()

arquivo.close()

# equacao de recorrencia : OPT(i,b) = max (j = 1…10) { (j*vi) + OPT(i - 1,b - (j * vi)) }

m = [[0 for _ in range(B+1)] for _ in range(n+1)]
qtdItens = [[0 for _ in range(B+1)] for _ in range(n+1)]
      
def Knapsack(i,b,m,valor,tam,qtdItens):
    if i == 0 or b == 0:
        return 0
    
    maior = -1000000
    
    for n in range(1,i+1):
        for w in range(1,b+1):
            m[n][w] = m[n-1][w]
            for j in range(1,11):
                if j * tam[n-1] <= w:
                    m[n][w] = max(m[n][w], j * valor[n-1] + m[n-1][w - j * tam[n-1]])
                    if m[n][w] > maior:
                        maior = m[n][w]
                        qtdItens[n][w] = j
    
    return maior, qtdItens
    

def imprimeResultado(maior,qtdItens,indArq):
    print("Melhor valor obtido na instancia ",indArq,": ", maior,"\n")
    for i in range(1,n+1):
        print("Foram usados ",qtdItens[i][B]," do item numero ", i,"\n")

maior,qtdItens = Knapsack(n,B,m,valor,tam,qtdItens)
imprimeResultado(maior,qtdItens,1)

        
