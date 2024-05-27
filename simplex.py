import numpy as np
import time

def negative(line, var, res):
    for i in range(var-res):
        if(line[i] < 0):
            return True

    return False

def inVet(vet, j):
    for n in vet:
        if (n == j):
            return True
    return False
                

def simplex(var, res, fun, matrix):
    init = time.time()
    it = 1
    mat = np.array(matrix, dtype=float)
    b = res - 1
    vet = []
    for n in range(res):
        vet.append(b)
        b += 1
    print("Iteração {}:".format(it))
    print("Tempo (s): ", ("{:.4f}".format(time.time()-init)))
    print("Objetivo: ", ("{:.4f}".format(mat[0][var])))
    while(negative(mat[0], var, res)):
        it += 1
        i = 0
        j = 0
        min = 0
        for a in range(var+1):
            if(mat[0][a] < min):
                min = mat[0][a]
                j = a
        find = True
        min = 0
        for a in range(res+1):
            if (mat[a][j] > 0):
                if(find):
                    min = mat[a][var]/mat[a][j]
                    i = a
                    find = False
                else:
                    if ((mat[a][var]/mat[a][j]) < min):
                        min = mat[a][var]/mat[a][j]
                        i = a
        for a in range(res):
            if (vet[a] == i):
                vet[a] = j
                break
        if(mat[i][j] != 1):
            b = 1/mat[i][j]
            for jj in range(var+1):
                mat[i][jj] *= b
        for l in range(res+1):
            if(l != i):
                a = np.array([mat[l][j]*(-1)])
                line = np.array(mat[i])
                line = line*a
                for c in range(var+1):
                    mat[l][c] = mat[l][c]+line[c]
        print("\nIteração {}:".format(it))
        print("Tempo (s): ", ("{:.4f}".format(time.time()-init)))
        print("Objetivo: ", ("{:.4f}".format(mat[0][var]*(-1))))
        

    print("\nSolução ótima encontrada em {:.4f} segundos!".format(time.time()-init))
    print("Função objetivo é {:.4f}.".format(mat[0][var]*(-1)))
    print("\nSolução:")
    x = []
    line = mat[0]
    for l in range(var):
        if (line[l] == 0):
            x.append(1)
        else:
            x.append(0)
    x = np.array(x)
    newMat = []
    result = []
    for i in range(res):
        i += 1
        line = []
        for j in range(var+1):
            if (j == var):
                result.append(mat[i][j])
            else:
                line.append(mat[i][j])
        newMat.append(line)
    newMat = np.array(newMat, dtype=float)
    exclude = []
    for j in range(var):
        if(x[j] == 0):
           exclude.append(j)
        elif (np.all(newMat[:, j] == 0)):
            exclude.append(j)
            x[j] = 0
    result = np.array(result, dtype=float)
    newMat = np.delete(newMat, exclude, axis=1)
    solution = np.linalg.solve(newMat, result)
    s = 0
    for i in range(var):
        if (x[i] == 0):
            print("x[{}] = 0.0000".format((i+1)))
        else:
            print("x[{}] = {:.4f}".format((i+1), solution[s]))
            s += 1
    

    


