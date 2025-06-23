from array import array
import os
import time

class PilhaCheiaErro(Exception): pass
class PilhaVaziaErro(Exception): pass
class TipoErro(Exception): pass

class Pilha:
    def __init__(self, capacidade, tipo_dado):
        if tipo_dado not in ['i', 'u']:
            raise ValueError("Tipo de dado inválido. Use 'i' para inteiros ou 'u' para caracteres.")
        self.dados = array(tipo_dado)
        self.capacidade = capacidade
        self.tipo_dado = tipo_dado

    def empilha(self, dado):
        if self.tipo_dado == 'i' and not isinstance(dado, int):
            raise TipoErro("Tipo de dado inválido, deve ser inteiro")
        if self.tipo_dado == 'u' and not isinstance(dado, str) or (isinstance(dado, str) and len(dado) != 1):
            raise TipoErro("Tipo de dado inválido, deve ser um único caractere")

        if self.pilha_esta_cheia():
            raise PilhaCheiaErro("A pilha está cheia")
        self.dados.append(dado)

    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("A pilha está vazia")
        return self.dados.pop()

    def pilha_esta_vazia(self):
        return len(self.dados) == 0

    def pilha_esta_cheia(self):
        return len(self.dados) >= self.capacidade

    def troca(self):
        if len(self.dados) < 2:
            raise PilhaVaziaErro("Pilha precisa ter pelo menos 2 elementos para trocar")
        self.dados[-1], self.dados[-2] = self.dados[-2], self.dados[-1]

    def tamanho(self):
        return len(self.dados)

def preencher_regiao_pilha(matriz, linha_inicial, coluna_inicial, passos_visualizacao):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    
    if not (0 <= linha_inicial < n_linhas and 0 <= coluna_inicial < n_colunas):
        print("Coordenadas fora dos limites da matriz")
        return
    
    if matriz[linha_inicial][coluna_inicial] != '1':
        print("Posição inicial não contém '1' para preencher")
        return

    capacidade_pilha = n_linhas * n_colunas
    pilha = Pilha(capacidade_pilha, 'i') # Usando 'i' para inteiros para armazenar posições
    pos_inicial = linha_inicial * n_colunas + coluna_inicial
    pilha.empilha(pos_inicial)
    
    contador_passos = 0

    while not pilha.pilha_esta_vazia():
        pos = pilha.desempilha()
        linha, coluna = divmod(pos, n_colunas)

        if matriz[linha][coluna] != '1':
            continue

        matriz[linha][coluna] = '0'
        contador_passos += 1

        if passos_visualizacao > 0 and contador_passos % passos_visualizacao == 0:
            imprimir_matriz_visual(matriz)
            input("Pressione ENTER para continuar...")

        vizinhos = [
            (linha-1, coluna), (linha+1, coluna),
            (linha, coluna-1), (linha, coluna+1)
        ]

        for l, c in vizinhos:
            if 0 <= l < n_linhas and 0 <= c < n_colunas:
                if matriz[l][c] == '1':
                    pilha.empilha(l * n_colunas + c)

def preencher_regiao_recursiva(matriz, linha, coluna, passos_visualizacao, contador_passos):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    
    if not (0 <= linha < n_linhas and 0 <= coluna < n_colunas):
        return
    
    if matriz[linha][coluna] != '1':
        return

    matriz[linha][coluna] = '0'
    contador_passos[0] += 1

    if passos_visualizacao > 0 and contador_passos[0] % passos_visualizacao == 0:
        imprimir_matriz_visual(matriz)
        input("Pressione ENTER para continuar...")

    preencher_regiao_recursiva(matriz, linha-1, coluna, passos_visualizacao, contador_passos)
    preencher_regiao_recursiva(matriz, linha+1, coluna, passos_visualizacao, contador_passos)
    preencher_regiao_recursiva(matriz, linha, coluna-1, passos_visualizacao, contador_passos)
    preencher_regiao_recursiva(matriz, linha, coluna+1, passos_visualizacao, contador_passos)
    

def ler_matriz_arquivo(caminho):
    if not os.path.exists(caminho):
        print(f"Arquivo '{caminho}' não encontrado")
        return None
    
    with open(caminho, 'r') as f:
        linhas = f.readlines()
    
    matriz = []
    for linha in linhas:
        linha_limpa = linha.strip()
        if linha_limpa:
            matriz.append(list(linha_limpa))
    
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(''.join(linha))

def imprimir_matriz_visual(matriz):
    for linha in matriz:
        linha_visual = ''
        for char in linha:
            if char == '1':
                linha_visual += ' '
            else:
                linha_visual += '#'
        print(linha_visual)

def copiar_matriz(matriz):
    nova_matriz = []
    for linha in matriz:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(elemento)
        nova_matriz.append(nova_linha)
    return nova_matriz

def obter_coordenadas_validas(n_linhas, n_colunas):
    while True:
        try:
            linha = int(input(f"Digite a linha inicial (0-{n_linhas-1}): "))
            coluna = int(input(f"Digite a coluna inicial (0-{n_colunas-1}): "))
            
            if 0 <= linha < n_linhas and 0 <= coluna < n_colunas:
                return linha, coluna
            else:
                print(f"Coordenadas inválidas. Linha: 0-{n_linhas-1}, Coluna: 0-{n_colunas-1}")
        except ValueError:
            print("Digite apenas números inteiros")

def obter_passos_visualizacao():
    while True:
        try:
            passos = int(input("Digite o número de passos entre visualizações (0 para executar sem paradas): "))
            if passos >= 0:
                return passos
            else:
                print("Digite um valor maior ou igual a 0")
        except ValueError:
            print("Digite apenas números inteiros")

def escolher_metodo():
    while True:
        print("\nEscolha o método de preenchimento:")
        print("1 - Usando Pilha (iterativo)")
        print("2 - Usando Recursão")
        opcao = input("Digite sua opção (1 ou 2): ")
        
        if opcao == '1':
            return 'pilha'
        elif opcao == '2':
            return 'recursiva'
        else:
            print("Opção inválida. Digite 1 ou 2")

def main():
    caminho = 'matriz.txt'
    
    matriz = ler_matriz_arquivo(caminho)
    if matriz is None:
        return
    
    n_linhas = len(matriz)
    n_colunas = len(matriz[0]) if matriz else 0
    
    if n_linhas == 0 or n_colunas == 0:
        print("Matriz vazia ou inválida")
        return
    
    print("Matriz original:")
    imprimir_matriz(matriz)
    print()
    
    linha_inicial, coluna_inicial = obter_coordenadas_validas(n_linhas, n_colunas)
    passos_visualizacao = obter_passos_visualizacao()
    metodo = escolher_metodo()
    
    matriz_copia = copiar_matriz(matriz)
    
    print(f"\nIniciando preenchimento usando {metodo}...")
    print("Visualização: ' ' = 1, '#' = 0")
    print()
    
    if passos_visualizacao > 0:
        print("Matriz inicial (visual):")
        imprimir_matriz_visual(matriz_copia)
        input("Pressione ENTER para iniciar...")
    
    if metodo == 'pilha':
        preencher_regiao_pilha(matriz_copia, linha_inicial, coluna_inicial, passos_visualizacao)
    else:
        contador_passos = [0]
        preencher_regiao_recursiva(matriz_copia, linha_inicial, coluna_inicial, passos_visualizacao, contador_passos)
    
    print("\nMatriz final:")
    imprimir_matriz(matriz_copia)
    print("\nMatriz final (visual):")
    imprimir_matriz_visual(matriz_copia)

if __name__ == "__main__":
    main()

