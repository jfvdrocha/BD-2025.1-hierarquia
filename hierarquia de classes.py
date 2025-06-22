from abc import ABC, abstractmethod

class EstruturaLinearVaziaError(Exception):
    pass

class EstruturaLinear(ABC):
    @abstractmethod
    def inserir(self, valor):
        pass

    @abstractmethod
    def remover(self):
        pass

    @abstractmethod
    def consultar(self):
        pass

# Implementação de Array
class Array(EstruturaLinear):
    def __init__(self):
        self.dados = []

    def inserir(self, valor):
        self.dados.append(valor)

    def remover(self):
        if not self.dados:
            raise EstruturaLinearVaziaError("Array vazio. Não é possível remover.")
        return self.dados.pop()

    def consultar(self):
        return self.dados.copy()

class Pilha(EstruturaLinear):
    def __init__(self):
        self.itens = []

    def inserir(self, valor):
        self.itens.append(valor)

    def remover(self):
        if not self.itens:
            raise EstruturaLinearVaziaError("Pilha vazia. Não é possível desempilhar.")
        return self.itens.pop()

    def consultar(self):
        return self.itens[-1] if self.itens else None

class Fila(EstruturaLinear):
    def __init__(self):
        self.itens = []

    def inserir(self, valor):
        self.itens.append(valor)

    def remover(self):
        if not self.itens:
            raise EstruturaLinearVaziaError("Fila vazia. Não é possível desenfileirar.")
        return self.itens.pop(0)

    def consultar(self):
        return self.itens[0] if self.itens else None

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada(EstruturaLinear):
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo_no = No(valor)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover(self):
        if not self.cabeca:
            raise EstruturaLinearVaziaError("Lista encadeada vazia. Não é possível remover.")
        valor = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        return valor

    def consultar(self):
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos

def testar_estrutura(estrutura):
    print("Inserindo 1, 2, 3...")
    estrutura.inserir(1)
    estrutura.inserir(2)
    estrutura.inserir(3)
    print("Estado atual:", estrutura.consultar())
    print("Removendo:", estrutura.remover())
    print("Estado atual:", estrutura.consultar())

if __name__ == "__main__":
    for estrutura in [Array(), Pilha(), Fila(), ListaEncadeada()]:
        print("\nTestando:", estrutura.__class__.__name__)
        try:
            testar_estrutura(estrutura)
        except EstruturaLinearVaziaError as e:
            print("Erro:", e)
