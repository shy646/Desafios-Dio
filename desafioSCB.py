saldo = 0.0
limiteSaqueDiario = 500.0
saquesRealizados = []
depositosRealizados = []
LIMITE_SAQUES = 3


def realizar_deposito(valor):
    global saldo
    saldo += valor
    depositosRealizados.append(valor)


def realizar_saque(valor):
    global saldo
    if saldo >= valor and len(saquesRealizados) < 3 and valor <= limiteSaqueDiario:
        saldo -= valor
        saquesRealizados.append(valor)
    else:
        print("Não é possível realizar o saque.")


def exibir_extrato():
    if not depositosRealizados and not saquesRealizados:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        print("Depósitos:")
        for deposito in depositosRealizados:
            print("R$ {:.2F}".format(deposito))
        print("Saques:")
        for saque in saquesRealizados:
            print("R$ {:.2f}".format(saque))
        print("Saldo atual: R$ {:.2F}".format(saldo))


def exibir_menu():
    print("===== MENU =====")
    print("[1] Realizar Depósito")
    print("[2] Relizar Saque")
    print("[3] Exibir extrato")
    print("[4] Sair")


exibir_menu()
opcao = 0

while opcao != 4:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor do depósito: "))
        realizar_deposito(valor_deposito)
        print("Depósito realizado.")
    elif opcao == 2:
        valor_saque = float(input("Digite o valor do saque: "))
        realizar_saque(valor_saque)
        print("Saqu realizado.")
    elif opcao == 3:
        exibir_extrato()
    elif opcao == 4:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

    print()  # linha em branco para separar as opções

    print("Obrigado por utilizar nosso sistema bancário.")
