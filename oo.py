# %%
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def apresentar(self):
        print(f'Olá! Meu nome é {self.nome} e tenho {self.idade} anos!', end = ' ')
        print(f'Atualmente estou morando em {self.endereco}!')
        return self.apresentar


pessoa01 = Pessoa('Jean', 19, 'Brasil')
pessoa02 = Pessoa('Eric', 18, 'Espirito Santo - Brasil')

print(pessoa01.apresentar())
print(pessoa02.apresentar())

# %%
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, desposito):
        self.deposito = desposito
        self.saldo += desposito 

        return f'Deposito de R${self.deposito} realizado.'

    def sacar(self, saque):
        self.saque = saque
        self.saldo -= saque

        return f'Saque de R${self.saque} realizado.'
    
    def extrato(self, extrato):
        self.extrato = extrato

        if self.extrato == True:
            return f'Sua conta possui R${self.saldo} de saldo'
        else:
            return f'Visualização de saldo desativada.'


dadosBancarios = ContaBancaria('Jean', 100)


print(dadosBancarios.depositar(50))
print(dadosBancarios.sacar(25))
print(dadosBancarios.extrato(False))