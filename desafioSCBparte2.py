usuarios = []
contas = []
numero_conta = 1


def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    cpf_numeros = "".join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario["cpf"] == cpf_numeros:
            print("CPF já cadastrado.")
            return
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_numeros,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")


def cadastrar_conta_corrente(cpf):
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
    if usuario_encontrado is None:
        print("Usuário não encontrado.")
        return
    global numero_conta
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }
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
        extrato.append(valor)
    else:
        print("Não é possível realizar o saque.")
    return saldo, extrato


def exibir_extrato(saldo, *, extratos):
    if not extratos:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        print("Depósitos:")
        for deposito in extratos:
            print("R$ {:.2f}".format(deposito))
        print("Saldo atual: R$ {:.2f}".format(saldo))


def exibir_menu():
    print("===== MENU =====")
    print("[1] Cadastrar Usuário")
    print("[2] Cadastrar Conta Corrente")
    print("[3] Realizar Depósito")
    print("[4] Relizar Saque")
    print("[5] Exibir Extrato")
    print("[6] Sair")


saldo = 0.0
limite_saque_diario = 500.0
extrato = []
LIMITE_SAQUES = 3

exibir_menu()
opcao = 0

while opcao != 6:
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
        saldo, extrato = realizar_deposito(
            saldo=saldo, valor=valor_deposito, extrato=extrato)
        print("Depósito realizado.")
    elif opcao == 4:
        valor_saque = float(input("Digite o valor do saque: "))
        saldo, extrato = realizar_saque(saldo=saldo, valor=valor_saque, extrato=extrato,
                                        limite=limite_saque_diario, numero_saques=len(extrato), limite_saques=LIMITE_SAQUES)
        print("Saque realizado.")
    elif opcao == 5:
        exibir_extrato(saldo=saldo, extratos=extrato)
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

        print()  # linha em branco para separar as opções
