# Inicialização das variáveis do sistema bancário
saldo = 3000.0
limite = 500.0
extrato = []

print("Sistema Bancário Inicializado!")
print(f"Saldo inicial: R$ {saldo:.2f}")
print(f"Limite por saque: R$ {limite:.2f}")
print("Extrato: (vazio)")
print("-" * 30)

while True:
    print("\nEscolha uma operação:")
    print("1 - Consultar Saldo")
    print("2 - Realizar Saque")
    print("3 - Visualizar Extrato")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        # Lógica para consultar saldo
        print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
    elif opcao == '2':
        # Lógica para realizar saque
        valor_saque_str = input("Digite o valor que deseja sacar: R$ ")
        try:
            valor_saque = float(valor_saque_str)
            if valor_saque <= 0:
                print("Valor inválido. Por favor, digite um valor positivo.")
            elif valor_saque > limite:
                print(f"Valor inválido. O limite por saque é de R$ {limite:.2f}.")
            elif valor_saque > saldo:
                print("Saldo em conta insuficiente.")
            else:
                saldo -= valor_saque
                extrato.append(f"Saque: R$ {valor_saque:.2f} - Saldo restante: R$ {saldo:.2f}")
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    elif opcao == '3':
        # Lógica para visualizar extrato
        if extrato:
            print("\n----- Extrato -----")
            for registro in extrato:
                print(registro)
            print("-------------------")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("\nNão foram realizados saques.")
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == '4':
        print("Obrigado por usar o Sistema Bancário!")
        break  # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 4.")

    print("-" * 30) # Separador entre as operações