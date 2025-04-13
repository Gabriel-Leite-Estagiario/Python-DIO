from datetime import datetime

# Dicionário para armazenar informações dos usuários (simulação)
usuarios = {}
# Dicionário para armazenar informações das contas (simulação)
contas = {}
proxima_conta = 1

def criar_usuario(usuarios):
    """Cria um novo usuário."""
    cpf = input("Digite o CPF do novo usuário (apenas números): ")
    if cpf in usuarios:
        print("CPF já cadastrado.")
        return
    nome = input("Digite o nome completo do novo usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite o endereço completo (rua, número - bairro - cidade/UF): ")
    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "contas": []}
    print("Usuário criado com sucesso!")

def criar_conta(usuarios, contas, proxima_conta):
    """Cria uma nova conta bancária para um usuário existente."""
    cpf = input("Digite o CPF do titular da conta (apenas números): ")
    if cpf not in usuarios:
        print("Usuário não encontrado.")
        return proxima_conta  # Retorna proxima_conta inalterada se o usuário não existe

    nova_conta = {"agencia": "0001", "numero": str(proxima_conta).zfill(6), "saldo": 0.0, "extrato": []}
    contas[nova_conta["numero"]] = nova_conta
    usuarios[cpf]["contas"].append(nova_conta["numero"])
    print(f"Conta nº {nova_conta['numero']} criada com sucesso para o usuário {usuarios[cpf]['nome']}.")
    return proxima_conta + 1

def listar_contas(contas, usuarios):
    """Lista todas as contas bancárias existentes e seus titulares."""
    if not contas:
        print("Não há contas cadastradas.")
        return
    print("\n----- Listagem de Contas -----")
    for numero_conta, info_conta in contas.items():
        titulares = [usuarios[cpf]["nome"] for cpf, dados_usuario in usuarios.items() if numero_conta in dados_usuario["contas"]]
        print(f"Agência: {info_conta['agencia']} | Conta: {numero_conta} | Titular(es): {', '.join(titulares)} | Saldo: R$ {info_conta['saldo']:.2f}")
    print("-----------------------------\n")

def consultar_saldo(contas, numero_conta):
    """Exibe o saldo atual de uma conta específica."""
    if numero_conta in contas:
        print(f"\nSaldo da conta {numero_conta}: R$ {contas[numero_conta]['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

def realizar_saque(contas, numero_conta, limite):
    """Realiza a operação de saque em uma conta específica."""
    if numero_conta not in contas:
        print("Conta não encontrada.")
        return

    valor_saque_str = input("Digite o valor que deseja sacar: R$ ")
    try:
        valor_saque = float(valor_saque_str)
        if valor_saque <= 0:
            print("Valor inválido. Por favor, digite um valor positivo.")
        elif valor_saque > limite:
            print(f"Valor inválido. O limite por saque é de R$ {limite:.2f}.")
        elif valor_saque > contas[numero_conta]['saldo']:
            print("Saldo em conta insuficiente.")
        else:
            contas[numero_conta]['saldo'] -= valor_saque
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            contas[numero_conta]['extrato'].append(f"{data_hora} - Saque: R$ {valor_saque:.2f} - Saldo restante: R$ {contas[numero_conta]['saldo']:.2f}")
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso na conta {numero_conta}.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

def realizar_deposito(contas, numero_conta):
    """Realiza a operação de depósito em uma conta específica."""
    if numero_conta not in contas:
        print("Conta não encontrada.")
        return

    valor_deposito_str = input("Digite o valor que deseja depositar: R$ ")
    try:
        valor_deposito = float(valor_deposito_str)
        if valor_deposito <= 0:
            print("Valor inválido. Por favor, digite um valor positivo.")
        else:
            contas[numero_conta]['saldo'] += valor_deposito
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            contas[numero_conta]['extrato'].append(f"{data_hora} - Depósito: R$ {valor_deposito:.2f} - Saldo restante: R$ {contas[numero_conta]['saldo']:.2f}")
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso na conta {numero_conta}.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

def visualizar_extrato(contas, numero_conta):
    """Exibe o extrato de uma conta específica."""
    if numero_conta not in contas:
        print("Conta não encontrada.")
        return

    extrato = contas[numero_conta]['extrato']
    saldo = contas[numero_conta]['saldo']
    if extrato:
        print(f"\n----- Extrato da Conta {numero_conta} -----")
        for registro in extrato:
            print(registro)
        print("---------------------------------------")
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print(f"\nNão foram realizadas transações na conta {numero_conta}.")
        print(f"Saldo atual: R$ {saldo:.2f}")

print("Sistema Bancário Inicializado!")
print("-" * 30)

while True:
    print("\nEscolha uma operação:")
    print("1 - Novo Usuário")
    print("2 - Nova Conta")
    print("3 - Listar Contas")
    print("4 - Consultar Saldo")
    print("5 - Realizar Saque")
    print("6 - Realizar Depósito")
    print("7 - Visualizar Extrato")
    print("8 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        criar_usuario(usuarios)
    elif opcao == '2':
        novo_numero_conta = criar_conta(usuarios, contas, proxima_conta)
        if novo_numero_conta:
            proxima_conta = novo_numero_conta
    elif opcao == '3':
        listar_contas(contas, usuarios)
    elif opcao == '4':
        numero_conta_consulta = input("Digite o número da conta para consultar o saldo: ")
        consultar_saldo(contas, numero_conta_consulta)
    elif opcao == '5':
        numero_conta_saque = input("Digite o número da conta para realizar o saque: ")
        realizar_saque(contas, numero_conta_saque, 500.0) # O limite ainda está fixo aqui
    elif opcao == '6':
        numero_conta_deposito = input("Digite o número da conta para realizar o depósito: ")
        realizar_deposito(contas, numero_conta_deposito)
    elif opcao == '7':
        numero_conta_extrato = input("Digite o número da conta para visualizar o extrato: ")
        visualizar_extrato(contas, numero_conta_extrato)
    elif opcao == '8':
        print("Obrigado por usar o Sistema Bancário!")
        break
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 8.")

    print("-" * 30)