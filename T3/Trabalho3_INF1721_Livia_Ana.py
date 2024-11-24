

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
print(valor)

m = []

for i in range(0,n):
    m.append([])
    for j in range(0,B):
        m[i].append(0)
        
print(m[0][0])

def Knapsack(i,b):
    maior = -10000000000
    qtdItens = 0
    for k in range(1,i):
        for j in range(0,9):
            print("k = ", k)
            print("j = ", j)
            if((j * valor[k]) <= b):
                max = (j * valor[k]) + m[k-1][b - (j * valor[k])]
                if max > maior:
                    maior = max
                    qtdItens +=1
    m[i][b] = maior
    return maior, qtdItens

def imprimeResultado(maior,qtdItens,indArq):
    print("Melhor valor obtido na instancia ",indArq,": ", maior,"\n")
    for i in range(0,n):
        print("Foram usados", qtdItens, "do item numero", i,"\n")

maior, qtdItens = Knapsack(n,B)
imprimeResultado(maior,qtdItens,1)
        
