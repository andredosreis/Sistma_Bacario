from Cliente.cliente import Cliente

class Conta:

    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente()
        self.historico = Historico()

    @classmethod
    def criar_conta(cls, numero, cliente):
        return cls(numero, cliente)

#mapeando os metodos da classe cliente
    @property
    def saldo(self):
        return self._saldo
    
    @property()
    def cliente(self):
        return self._cliente
    
    @property()
    def numero(self):
        return self._numero
    
    @property()
    def agencia(self):
        return self._agencia

    @property()
    def historico(self):
        return self._historico
    

    def sacar(self, valor):
        saldo = self.saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:
            print('\n@@@ Operação falhou Saldo insuficiente. @@@')
            return False
        elif valor > 0:
            self._saldo -= valor
            print('\n@@@ Operação realizada com sucesso. @@@')
            return True

        else:
            print('\n@@@ Operação falhou! o valor informado é inválido @@@')
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n@@@ Operação realizada com sucesso. @@@')
            
        else:
            print('\n@@@ Operação falhou! o valor informado é inválido @@@')
            return False

        return True

class ContaCorrente(Conta):

    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limete_de_saques = limete_de_saques
    
    def sacar(self, valor):
        numero_de_saques = len([])
    

    


