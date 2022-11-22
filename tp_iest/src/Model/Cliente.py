from datetime import date
from .Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self):
        self.rg = ''
        self.dataDeNascimento = date

    def toString(self):
        return f"Nome: {self.nome}\n\
Endereço: {self.endereco}\n\
RG: {self.rg}\n\
Data de Nascimento: {self.dataDeNascimento.strftime('%d/%m/%Y')}\n\n"

    def setAll(self, bd):
        print('Digite os dados do cliente:')
        print('Nome:')
        self.nome = input()
        print('Endereço:')
        self.endereco = input()
        print('RG:')
        self.rg = input()
        print('Data de Nascimento (dia/mes/ano):')
        dataFormatada = input()
        [dia, mes, ano] = dataFormatada.split('/')
        self.dataDeNascimento = date(int(ano), int(mes), int(dia))

    def alter(self, bd):
        print('Digite os novos dados do cliente: (deixe em branco para não alterar)')
        print('Nome:')
        buffer = input()
        if buffer != '':
            self.nome = buffer
        print('Endereço:')
        buffer = input()
        if buffer != '':
            self.endereco = buffer
        print('RG:')
        buffer = input()
        if buffer != '':
            self.rg = buffer
        print('Data de Nascimento (dia/mes/ano):')
        buffer = input()
        if buffer != '':
            [dia, mes, ano] = buffer.split('/')
            self.dataDeNascimento = date(int(ano), int(mes), int(dia))
    
    def getKey(self):
        return self.rg

    def getNome(self):
        return self.nome