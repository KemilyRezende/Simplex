import input
import simplex

def main():
    # Lê as variáveis
    var, res, fun, matrix = input.input()
    simplex.simplex(var, res, fun, matrix)

if __name__ == "__main__":
    main()