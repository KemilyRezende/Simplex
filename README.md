# Simplex

Este projeto tem como objetivo implementar o Algoritmo Simplex para resolver Problemas de Minimização em Programação Linear. O Simplex é um método poderoso para otimizar funções lineares sujeitas a restrições lineares e é amplamente utilizado em áreas como economia, engenharia e ciência da computação.

## Tecnologias

### Python

A escolha da linguagem Python para este trabalho se baseia em sua simplicidade de escrita e na ampla variedade de ferramentas disponibilizadas por bibliotecas como o `NumPy`. Essas bibliotecas facilitam o desenvolvimento da solução e a tornam mais precisa. Além disso, a continuidade com o trabalho de Enumeração de Soluções também foi um fator relevante na decisão.

### Bibliotecas

- `NumPy:` fornece suporte para arrays e matrizes multidimensionais, além de funções matemáticas para operar nesses arrays.
- `sys:` fornece acesso a algumas variáveis e funções que interagem fortemente com o interpretador Python.

## Estrutura

O código é dividido em 3 arquivos para manter a organização e legibilidade.
- `input.py:` Responsável por gerenciar a entrada de dados, incluindo a leitura do arquivo de entrada e o processamento das informações necessárias para a resolução do problema.
- `simplex.py:` Contém a implementação do algoritmo Simplex. Ele executa cada iteração do algoritmo e exibe o número da iteração, o tempo decorrido e o valor da função objetivo. Quando encontra a solução ótima, também calcula os valores das variáveis de decisão e folga.
- `main.py:` O ponto de entrada do programa, que coordena a execução das funcionalidades definidas nos outros arquivos.

## Execução

Para executar o programa é necessário o seguinte comando:

```bash
python3 main.py arquivo_de_entradas.txt
```
Este comando iniciará o processo de resolução do problema de programação linear, utilizando as informações contidas no arquivo de entradas fornecido como argumento.

