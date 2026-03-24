class Paciente:
    def __init__(self, nome, prioritario):
        self.nome = nome
        self.prioritario = prioritario


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

    def inserir_inicio(self, valor):
        novo = No(valor)

        # verifica se a lista está vazia
        if self.tamanho == 0:
            self.fim = novo
        else:
            novo.dir = self.inicio
            self.inicio.esq = novo

        self.inicio = novo
        self.tamanho += 1

    def inserir_final(self, valor):
        novo = No(valor)

        # verifica se a lista está vazia
        if self.tamanho == 0:
            self.inicio = novo
        else:
            self.fim.dir = novo
            novo.esq = self.fim

        self.fim = novo
        self.tamanho += 1

    def inserir(self, nome, prioritario):
        paciente = Paciente(nome, prioritario)

        # lista vazia
        if self.tamanho == 0:
            self.inserir_inicio(paciente)

        # paciente comum entra no final
        elif prioritario == False:
            self.inserir_final(paciente)

        # paciente prioritário
        else:
            # se o primeiro não é prioritário, entra no início
            if self.inicio.dado.prioritario == False:
                self.inserir_inicio(paciente)
            else:
                aux = self.inicio

                # procura o último prioritário
                while aux.dir is not None and aux.dir.dado.prioritario == True:
                    aux = aux.dir

                novo = No(paciente)

                # inserir depois do último prioritário
                if aux == self.fim:
                    self.fim.dir = novo
                    novo.esq = self.fim
                    self.fim = novo
                else:
                    novo.dir = aux.dir
                    novo.esq = aux
                    aux.dir.esq = novo
                    aux.dir = novo

                self.tamanho += 1

    def atender(self):
        if self.tamanho == 0:
            return None

        removido = self.inicio
        paciente = removido.dado

        # lista com apenas um elemento
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None

        # remove o primeiro
        else:
            self.inicio = removido.dir
            self.inicio.esq = None
            removido.dir = None

        self.tamanho -= 1
        return paciente

    def exibir(self):
        if self.tamanho == 0:
            print("Fila vazia")
            return

        aux = self.inicio
        posicao = 0

        while aux is not None:
            if aux.dado.prioritario == True:
                tipo = "PRIORITARIO"
            else:
                tipo = "COMUM"

            print("Posicao:", posicao, "- Nome:", aux.dado.nome, "- Tipo:", tipo)
            aux = aux.dir
            posicao += 1

    def buscar(self, nome):
        aux = self.inicio
        posicao = 0

        while aux is not None:
            if aux.dado.nome.lower() == nome.lower():
                if aux.dado.prioritario == True:
                    tipo = "PRIORITARIO"
                else:
                    tipo = "COMUM"

                return posicao, tipo

            aux = aux.dir
            posicao += 1

        return None


def gerar_menu():
    print()
    print("[1] Inserir paciente")
    print("[2] Atender paciente")
    print("[3] Exibir fila")
    print("[4] Buscar paciente")
    print("[5] Encerrar")


# programa principal
fila = Lista()

while True:
    gerar_menu()
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        nome = input("Informe o nome do paciente: ")
        resp = input("Paciente prioritario? (s/n): ").lower()

        while resp != "s" and resp != "n":
            resp = input("Digite apenas s ou n: ").lower()

        if resp == "s":
            prioritario = True
        else:
            prioritario = False

        fila.inserir(nome, prioritario)
        print("Paciente inserido!.")

    elif opcao == 2:
        paciente = fila.atender()

        if paciente is None:
            print("Fila vazia")
        else:
            if paciente.prioritario == True:
                tipo = "PRIORITARIO"
            else:
                tipo = "COMUM"

            print("Paciente atendido:", paciente.nome, "-", tipo)

    elif opcao == 3:
        fila.exibir()

    elif opcao == 4:
        nome = input("Informe o nome do paciente que deseja buscar: ")
        resultado = fila.buscar(nome)

        if resultado is None:
            print("Paciente nao encontrado")
        else:
            print("Posicao:", resultado[0], "- Tipo:", resultado[1])

    elif opcao == 5:
        print("Aplicacao encerrada")
        break

    else:
        print("Opcao invalida")