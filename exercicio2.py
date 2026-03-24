class Processo:
    def __init__(self, id_processo, nome, tempo_total):
        self.id = id_processo
        self.nome = nome
        self.tempo_total = tempo_total
        self.tempo_restante = tempo_total
        self.tempo_espera = 0
        self.tempo_retorno = 0


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

    def inserir_final(self, valor):
        novo = No(valor)

        # verifica se a lista está vazia
        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
        else:
            novo.esq = self.fim
            novo.dir = self.inicio
            self.fim.dir = novo
            self.inicio.esq = novo
            self.fim = novo

        self.tamanho += 1

    def remover_no(self, aux):
        if aux is not None:
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

            aux.esq = None
            aux.dir = None
            self.tamanho -= 1

    def imprimir(self):
        if self.tamanho == 0:
            print("Lista vazia")
            return

        aux = self.inicio
        for i in range(self.tamanho):
            print(aux.dado, end="  ")
            aux = aux.dir
        print()


def executar_processos(lista, fatia_tempo):
    tempo = 0
    finalizados = Lista()
    atual = lista.inicio

    while lista.tamanho > 0:
        processo = atual.dado

        if processo.tempo_restante > fatia_tempo:
            executado = fatia_tempo
        else:
            executado = processo.tempo_restante

        print("t =", tempo, "->", processo.nome, "executa", executado, "u", end="")

        processo.tempo_restante = processo.tempo_restante - executado
        tempo = tempo + executado

        if processo.tempo_restante == 0:
            processo.tempo_retorno = tempo
            processo.tempo_espera = processo.tempo_retorno - processo.tempo_total

            print(" | ✓ CONCLUIDO (terminou em t =", tempo, ")")

            if lista.tamanho == 1:
                proximo = None
            else:
                proximo = atual.dir

            lista.remover_no(atual)
            finalizados.inserir_final(processo)
            atual = proximo

        else:
            print(" | restam:", processo.tempo_restante, "u")
            atual = atual.dir

    return finalizados


def relatorio_final(finalizados, fatia_tempo):
    print()
    print("RELATORIO FINAL - ARIA Recovery Module")
    print("Fatia de tempo:", fatia_tempo, "unidades")
    print()
    print("  Processo     - Tempo Total - Tempo Espera - Tempo Retorno")

    soma_espera = 0
    soma_retorno = 0

    aux = finalizados.inicio
    for i in range(finalizados.tamanho):
        processo = aux.dado

        print(processo.nome, " - ", str(processo.tempo_total) + "u", " - ", str(processo.tempo_espera) + "u", " - ", str(processo.tempo_retorno) + "u")

        soma_espera = soma_espera + processo.tempo_espera
        soma_retorno = soma_retorno + processo.tempo_retorno
        aux = aux.dir

    media_espera = soma_espera / finalizados.tamanho
    media_retorno = soma_retorno / finalizados.tamanho

    print("Media -", str(media_espera) + "u", "-", str(media_retorno) + "u")

    if media_espera < 16:
        print()
        print("ARIA reativada com sucesso.")
        print("Tempo medio de espera abaixo do limite critico.")
        print("Synthetica esta salva.")
    else:
        print()
        print("Falha critica confirmada.")
        print("Iniciando protocolo de desligamento de emergencia.")


# programa principal
fila = Lista()

qtd = int(input("Informe a quantidade de processos: "))

for i in range(qtd):
    print()
    print("Processo", i + 1)
    id_processo = input("ID do processo: ")
    nome = input("Nome do processo: ")
    tempo_total = int(input("Tempo necessario: "))

    processo = Processo(id_processo, nome, tempo_total)
    fila.inserir_final(processo)

fatia_tempo = int(input("\nInforme a fatia de tempo da CPU: "))

while fatia_tempo <= 0:
    fatia_tempo = int(input("Informe um valor maior que zero: "))

print()
print("SIMULACAO DA EXECUÇAO")
finalizados = executar_processos(fila, fatia_tempo)

relatorio_final(finalizados, fatia_tempo)