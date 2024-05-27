import sys

# Define a função de leitura de dados do programa e trata os mesmos para a execução

def input(): 
    # Define que o arquivo de entradas deve ser passado como argumento na linha de comando
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo_de_entradas.txt")
        sys.exit(1)

    with open(sys.argv[1], 'r') as file: # Abre o arquivo
        lines = file.readlines()
        
        # Lê a quantidade de variáveis e restrições da primeira linha
        var, res = map(int, lines[0].split()) 

        # Lê os coeficientes da função objetivo
        fun = list(map(float, lines[1].split()))
        rg = 2 + res
        matrix = []
        fun.append(0)
        matrix.append(fun)
        # Lê a matriz dos coeficientes das restrições
        for line in lines[2:rg]:
            l = list(map(float, line.split()))
            matrix.append(l)
        
        

        # Retorna as variáveis
        return var, res, fun, matrix