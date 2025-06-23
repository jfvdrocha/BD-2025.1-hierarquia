from singly_linked_list import SinglyLinkedList

class PilhaCheiaErro(Exception): pass
class PilhaVaziaErro(Exception): pass
class TipoErro(Exception): pass

class Pilha:
    def __init__(self, tipo_dado):
        self.dados = SinglyLinkedList()
        self.tipo_dado = tipo_dado

    def empilha(self, dado):
        if self.tipo_dado == 'i' and not isinstance(dado, int):
            raise TipoErro("Tipo de dado inválido, deve ser inteiro")
        if self.tipo_dado == 'u' and (not isinstance(dado, str) or len(dado) != 1):
            raise TipoErro("Tipo de dado inválido, deve ser um único caractere")

        # Pilha com lista encadeada não tem limite de capacidade, a menos que a memória se esgote.
        # A exceção PilhaCheiaErro não é aplicável aqui, a menos que um limite artificial seja imposto.
        # Por enquanto, vamos remover a verificação de pilha cheia.
        # if self.pilha_esta_cheia():
        #     raise PilhaCheiaErro("A pilha está cheia")
        
        self.dados.insert_at_start(dado)

    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("A pilha está vazia")
        return self.dados.remove_from_start()

    def pilha_esta_vazia(self):
        return self.dados.is_empty()

    def pilha_esta_cheia(self):
        # Com lista encadeada, a pilha só estaria cheia se a memória do sistema se esgotasse.
        # Para os propósitos desta implementação, consideramos que nunca está cheia.
        return False

    def troca(self):
        if self.dados.__len__() < 2:
            raise PilhaVaziaErro("Pilha precisa ter pelo menos 2 elementos para trocar")
        
        # Obter os dois elementos do topo
        topo1 = self.dados.remove_from_start()
        topo2 = self.dados.remove_from_start()
        
        # Empilhar na ordem inversa
        self.dados.insert_at_start(topo1)
        self.dados.insert_at_start(topo2)

    def tamanho(self):
        return self.dados.__len__()


