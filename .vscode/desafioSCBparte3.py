from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, data_nascimento, cpf, endereco)


class Conta:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, cliente):
        super().__init__(agencia, numero_conta, cliente)
        self.saldo = 0.0
        self.extrato = []

    def realizar_deposito(self, valor):
        self.saldo += valor
        self.extrato.append(valor)

    def realizar_saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(-valor)
        else:
            print("Não é possível realizar o saque.")

    def exibir_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimentacao in self.extrato:
                if movimentacao > 0:
                    print("Depósito: R$ {:.2f}".format(movimentacao))
                else:
                    print("Saque: R$ {:.2f}".format(-movimentacao))
            print("Saldo atual: R$ {:.2f}".format(self.saldo))


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def exibir_transacoes(self):
        if not self.transacoes:
            print("Não foram realizadas transações.")
        else:
            print("Histórico de Transações:")
            for transacao in self.transacoes:
                print(transacao)


class Transacao(ABC):
    def __init__(self, data, valor):
        self.data = data
        self.valor = valor

    @abstractmethod
    def __str__(self):
        pass


class Saque(Transacao):
    def __str__(self):
        return "Saque - Data: {}, Valor: R$ {:.2f}".format(self.data, self.valor)


class Deposito(Transacao):
    def __str__(self):
        return "Depósito - Data: {}, Valor: R$ {:.2f}".format(self.data, self.valor)


usuarios = []
contas = []
numero_conta = 1
historico = Historico()


def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    cpf_numeros = "".join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario.cpf == cpf_numeros:
            print("CPF já cadastrado.")
            return
    usuario = PessoaFisica(nome, data_nascimento, cpf_numeros, endereco)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")


def cadastrar_conta_corrente(cpf):
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break
    if usuario_encontrado is None:
        print("Usuário não encontrado.")
        return
    global numero_conta
    conta = ContaCorrente("0001", numero_conta, usuario_encontrado)
    contas.append(conta)
    numero_conta += 1
    print("Conta corrente cadastrada com sucesso.")


def realizar_deposito(saldo, valor, extrato):
    saldo += valor
    extrato.append(valor)
    return saldo, extrato


def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo >= valor and len(extrato) < limite_saques and valor <= limite:
        saldo -= valor
        extrato.append(-valor)
        return saldo, extrato
    else:
        print("Não é possível realizar o saque.")
        return saldo, extrato


def exibir_extrato(saldo, *, extratos):
    if not extratos:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for movimentacao in extratos:
            if movimentacao > 0:
                print("Depósito: R$ {:.2f}".format(movimentacao))
            else:
                print("Saque: R$ {:.2f}".format(-movimentacao))
        print("Saldo atual: R$ {:.2f}".format(saldo))


def exibir_menu():
    print("===== MENU =====")
    print("[1] Cadastrar Usuário")
    print("[2] Cadastrar Conta Corrente")
    print("[3] Realizar Depósito")
    print("[4] Realizar Saque")
    print("[5] Exibir Extrato")
    print("[6] Exibir Histórico de Transações")
    print("[7] Sair")


exibir_menu()
opcao = 0

while opcao != 7:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)
    elif opcao == 2:
        cpf = input("Digite o CPF do usuário: ")
        cadastrar_conta_corrente(cpf)
    elif opcao == 3:
        valor_deposito = float(input("Digite o valor do depósito: "))
        cpf = input("Digite o CPF do usuário: ")
        conta_corrente = None
        for conta in contas:
            if conta.cliente.cpf == cpf:
                conta_corrente = conta
                break
        if conta_corrente is None:
            print("Conta corrente não encontrada.")
            continue
        conta_corrente.realizar_deposito(valor_deposito)
        historico.adicionar_transacao(Deposito(datetime.now(), valor_deposito))
        print("Depósito realizado.")
    elif opcao == 4:
        valor_saque = float(input("Digite o valor do saque: "))
        cpf = input("Digite o CPF do usuário: ")
        conta_corrente = None
        for conta in contas:
            if conta.cliente.cpf == cpf:
                conta_corrente = conta
                break
        if conta_corrente is None:
            print("Conta corrente não encontrada.")
            continue
        conta_corrente.realizar_saque(valor_saque)
        historico.adicionar_transacao(Saque(datetime.now(), valor_saque))
        print("Saque realizado.")
    elif opcao == 5:
        cpf = input("Digite o CPF do usuário: ")
        conta_corrente = None
        for conta in contas:
            if conta.cliente.cpf == cpf:
                conta_corrente = conta
                break
        if conta_corrente is None:
            print("Conta corrente não encontrada.")
            continue
        conta_corrente.exibir_extrato()
    elif opcao == 6:
        historico.exibir_transacoes()
    elif opcao == 7:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

    print()  # linha em branco para separar as opções
