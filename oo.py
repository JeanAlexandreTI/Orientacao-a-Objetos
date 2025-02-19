# %%
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def apresentar(self):
        print(f'Olá! Meu nome é {self.nome} e tenho {self.idade} anos!', end = ' ')
        print(f'Atualmente estou morando em {self.endereco}!')

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

# %%
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligadoDesligado(self, ligado):
        
        if ligado == True:
            return f'Carro ligado'
        else:
            return f'Carro desligado'
    
celta = Carro('Chevrolet Celta LT 1.O', 2014, 'Prata')
celtaLigado = Carro

print(celta.ligadoDesligado(True))

# %%

class Endereco:
    def __init__(self, rua, bairro, cidade):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        
    def exibirEndereco(self):
        return f'{self.rua}, {self.bairro} - {self.cidade}'
    
class Pessoa(Endereco):
    def __init__(self,nome, idade, rua, bairro, cidade):
        super().__init__(rua, bairro, cidade)
        self.nome = nome
        self.idade = idade

    def dados(self):
        return f'Dados da pessoa que receberá a encomenda: \nNome: {self.nome}\nIdade: {self.idade} anos'

    def permissaoReceberEncomenda(self):
        if self.idade >= 18:
            return f'A pessoa pode receber a encomenda.'
        else:
            return f'A pessoa não pode receber a encomenda.'

residencia = Endereco('Todos os Santos', 'Jardim do Vale', 'Vila Velha')
dono_residencia = Pessoa('Jean', 15, 'Todos os Santos', 'Jardim do Vale', 'Vila Velha')

print(dono_residencia.exibirEndereco())
print(dono_residencia.dados())
print(dono_residencia.permissaoReceberEncomenda())

# %%
class Animal:
    def __init__(self, nome, idade, fazerSom):
        self.nome = nome
        self.idade = idade
        self.fazerSom = fazerSom

class Cachorro(Animal):
    def __init__(self, latir, nome, idade, fazerSom):
        super().__init__(nome, idade, fazerSom)

        self.latir = latir

    def latido(self):
        if self.latir != None: 
            if self.fazerSom == True:
                print(self.latir)
                return f'O cachorro latiu!'
            else:
                return f'O cachorro está dormindo...'


dog = Animal('Bolinha', 6, True)
acaoDog = Cachorro('Auau', 'Bolinha', 6, False)

print(acaoDog.latido())
# %%
