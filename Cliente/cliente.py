
class Cliente:

    def __init__(self, endereço):
        self.endereço = endereço
        self.contas = []

    def realizar_transição(self, conta, transição):
        transição.resgistrar(conta)

    # adiciona a transição à conta
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFísica(Cliente):

    def __init__(self, endereço, nome, cpf, data_nascimento):
        super().__init__(endereço)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


   