menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def exibir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def realizar_deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def realizar_saque(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = realizar_deposito(valor, saldo, extrato)
            except ValueError:
                print("Operação falhou! Valor inválido.")
        
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = realizar_saque(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
            except ValueError:
                print("Operação falhou! Valor inválido.")
        
        elif opcao == "e":
            exibir_extrato(extrato, saldo)
        
        elif opcao == "q":
            print("Saindo...")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
