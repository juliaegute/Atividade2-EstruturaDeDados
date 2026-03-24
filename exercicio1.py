
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, dado, posicao=None):
        novo = No(dado)

        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
            novo.esq = novo
            novo.dir = novo
            self.tamanho += 1
            return

        if posicao is None or posicao > self.tamanho:
            novo.esq = self.fim
            novo.dir = self.inicio
            self.fim.dir = novo
            self.inicio.esq = novo
            self.fim = novo
            self.tamanho += 1
            return

        if posicao <= 1:
            novo.dir = self.inicio
            novo.esq = self.fim
            self.inicio.esq = novo
            self.fim.dir = novo
            self.inicio = novo
            self.tamanho += 1
            return

        # inserir no meio
        aux = self.inicio

        # vai até a posição desejada
        for i in range(1, posicao):
            aux = aux.dir

        novo.dir = aux
        novo.esq = aux.esq
        aux.esq.dir = novo
        aux.esq = novo

        self.tamanho += 1

    def imprimir(self):
        if self.tamanho == 0:
            print("Lista vazia")
            return

        aux = self.inicio
        for i in range(self.tamanho):
            print(aux.dado, end=" ")
            aux = aux.dir
        print()

    def remover(self, dado):
        if self.tamanho == 0:
            return

        aux = self.inicio

        for i in range(self.tamanho):
            if aux.dado == dado:
                if self.tamanho == 1:
                    self.inicio = None
                    self.fim = None

                elif aux == self.inicio:
                    self.inicio = aux.dir
                    self.inicio.esq = self.fim
                    self.fim.dir = self.inicio

                elif aux == self.fim:
                    self.fim = aux.esq
                    self.fim.dir = self.inicio
                    self.inicio.esq = self.fim

                else:
                    aux.esq.dir = aux.dir
                    aux.dir.esq = aux.esq

                self.tamanho -= 1
                return

            aux = aux.dir
 
 
 
# programa principal   
        
lista = Lista()

lista.inserir(20)
lista.inserir(30)
lista.inserir(40)

print("Lista inicial:")
lista.imprimir()

lista.inserir(10, 1)
print("Inserindo o número 10 na posição 1:")
lista.imprimir()

lista.inserir(99, 20)
print("Inserindo o número 99 na posição 20/última posição:")
lista.imprimir()

lista.remover(30)
print("Removendo o número 30 da lista:")
lista.imprimir()