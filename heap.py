from functools import total_ordering
import math
class MinHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
        
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        return 2*i

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        return 2*i+1

    def pai(self, i) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        return math.floor(i/2)



    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):
        pass

    def insere(self,item):
        pass

    def retira_min(self):
        pass

    def __str__(self):
        return str(self.arr_heap)

    def __repr__(self):
        return str(self)