from datetime import datetime
from abc import ABC, abstractmethod

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Transacao(ABC):
    def __init__(self, valor):
        self._valor = valor
        self._data = datetime.now()

    @property
    def valor(self):
        return self._valor

    @property
    def data(self):
        return self._data.strftime("%d/%m/%Y %H:%M:%S")

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def registrar(self, conta):
        conta.sacar(self.valor)

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

class Conta(ABC):
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
        cliente.adicionar_conta(self)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            deposito = Deposito(valor)
            self._historico.adicionar_transacao(deposito)
            return True
        else:
            print("Valor inválido para depósito.")
            return False

    @classmethod
    def nova_conta(cls, cliente, numero_conta, agencia):
        return cls(numero_conta, agencia, cliente)

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite=500.0, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        if valor > 0 and self._saques_realizados < self._limite_saques:
            if valor <= (self._saldo + self._limite):
                self._saldo -= valor
                saque = Saque(valor)
                self._historico.adicionar_transacao(saque)
                self._saques_realizados += 1
                return True
            else:
                print("Saldo insuficiente ou limite de saque excedido.")
                return False
        elif self._saques_realizados >= self._limite_saques:
            print(f"Limite diário de {self._limite_saques} saques atingido.")
            return False
        else:
            print("Valor inválido para saque.")
            return False

clientes = []
contas_bancarias = []

def criar_novo_cliente():
    nome = input("Digite o nome completo do cliente: ")
    cpf = input("Digite o CPF do cliente (apenas números): ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite o endereço completo (rua, número - bairro - cidade/UF): ")
    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")
    return cliente

def criar_nova_conta(cliente):
    numero_conta = len(contas_bancarias) + 1
    agencia = "0001"
    conta = ContaCorrente.nova_conta(cliente, numero_conta, agencia)
    contas_bancarias.append(conta)
    print(f"Conta nº {conta.numero} criada com sucesso para o cliente {cliente.nome}.")
    return conta

def listar_contas_sistema():
    if not contas_bancarias:
        print("Não há contas cadastradas.")
        return
    print("\n----- Listagem de Contas -----")
    for conta in contas_bancarias:
        print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Titular: {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}")
    print("-----------------------------\n")

def encontrar_conta(numero_conta):
    for conta in contas_bancarias:
        if str(conta.numero) == numero_conta:
            return conta
    return None

def realizar_operacao(operacao, numero_conta, valor=None):
    conta = encontrar_conta(numero_conta)
    if conta:
        if operacao == "sacar":
            saque = Saque(valor)
            conta.cliente.realizar_transacao(conta, saque)
            if saque in conta.historico.transacoes: # Verifica se a transação foi registrada
                print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {conta.numero}.")
        elif operacao == "depositar":
            deposito = Deposito(valor)
            conta.cliente.realizar_transacao(conta, deposito)
            if deposito in conta.historico.transacoes: # Verifica se a transação foi registrada
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta.numero}.")
        elif operacao == "extrato":
            print(f"\n----- Extrato da Conta {conta.numero} -----")
            if conta.historico.transacoes:
                for transacao in conta.historico.transacoes:
                    print(f"{transacao.data} - {type(transacao).__name__}: R$ {transacao.valor:.2f}")
            else:
                print("Não foram realizadas transações.")
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
            print("---------------------------------------\n")
        elif operacao == "saldo":
            print(f"Saldo da conta {conta.numero}: R$ {conta.saldo:.2f}")
    else:
        print("Conta não encontrada.")

print("Sistema Bancário (Modelo Orientado a Objetos)")
print("-" * 40)

while True:
    print("\nEscolha uma operação:")
    print("1 - Novo Cliente")
    print("2 - Nova Conta")
    print("3 - Listar Contas")
    print("4 - Consultar Saldo")
    print("5 - Realizar Saque")
    print("6 - Realizar Depósito")
    print("7 - Visualizar Extrato")
    print("8 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        criar_novo_cliente()
    elif opcao == '2':
        if clientes:
            cpf_cliente = input("Digite o CPF do cliente para criar a conta: ")
            cliente_encontrado = next((c for c in clientes if c.cpf == cpf_cliente), None)
            if cliente_encontrado:
                criar_nova_conta(cliente_encontrado)
            else:
                print("Cliente não encontrado.")
        else:
            print("Não há clientes cadastrados. Crie um cliente primeiro.")
    elif opcao == '3':
        listar_contas_sistema()
    elif opcao == '4':
        numero_conta = input("Digite o número da conta para consultar o saldo: ")
        realizar_operacao("saldo", numero_conta)
    elif opcao == '5':
        numero_conta = input("Digite o número da conta para realizar o saque: ")
        valor_saque_str = input("Digite o valor que deseja sacar: R$ ")
        try:
            valor_saque = float(valor_saque_str)
            realizar_operacao("sacar", numero_conta, valor_saque)
        except ValueError:
            print("Valor inválido.")
    elif opcao == '6':
        numero_conta = input("Digite o número da conta para realizar o depósito: ")
        valor_deposito_str = input("Digite o valor que deseja depositar: R$ ")
        try:
            valor_deposito = float(valor_deposito_str)
            realizar_operacao("depositar", numero_conta, valor_deposito)
        except ValueError:
            print("Valor inválido.")
    elif opcao == '7':
        numero_conta = input("Digite o número da conta para visualizar o extrato: ")
        realizar_operacao("extrato", numero_conta)
    elif opcao == '8':
        print("Obrigado por usar o Sistema Bancário!")
        break
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 8.")

    print("-" * 40)