from datetime import date
from .Totalizavel import Totalizavel
from .Cliente import Cliente
from .ItemVenda import ItemVenda

class Venda(Totalizavel):
    def __init__(self):
        super().__init__()
        self.numero = 0
        self.data = date.today()
        self.cliente = Cliente()
        self.itens = []

    def setAll(self, bd):
        print('Digite os dados da Venda:')
        self.numero = int(input(f"Número:\n"))
        data = input(f"Data:\n")
        [dia, mes, ano] = data.split('/')
        self.data = date(int(ano), int(mes), int(dia))
        rgCliente = input(f"RG do Cliente:\n")
        for cliente in bd['2']:
            if cliente.getKey() == rgCliente:
                self.cliente = cliente
        codigo = ''
        while True:
            codigo = input(f"Código do Calcado:\n")
            if codigo == '':
                break
            quantidade = input(f"Quantidade do produto vendido:\n")
            for produto in bd['3']:
                if produto.getKey() == codigo:
                    item = ItemVenda().setProduto(produto).setQuantidade(quantidade)
                    self.itens.append(item)
            


    def toString(self):
        string = f"Código: {self.numero}\n\
Data:{self.data.strftime('%d/%m/%Y')}\n\
Cliente: {self.cliente.getNome()}\n\
Itens:\n"
        for item in self.itens:
            string += f" {item.getQuantidade()} x {item.getNome()} {item.total()}\n"
        string += f"Total: {self.total()}"
        return string


    def alter(self, bd):
        print('Digite os novos dados da Venda: (deixe em branco para não alterar)')
        buffer = input(f"Número:\n")
        if buffer != '':
            self.numero = int(buffer)
        buffer = input(f"Data: (dia/mes/ano)\n")
        if buffer != '':
            [dia, mes, ano] = buffer.split('/')
            self.data = date(int(ano), int(mes), int(dia))
        buffer = input(f"RG do Cliente:\n")
        if buffer != '':
            for cliente in bd['2']:
                if cliente.getKey() == buffer:
                    self.cliente = cliente
        for item in self.itens:
            buffer = input(f"Manter {item.getQuantidade()} x {item.getNome()}? (s/n)\n")
            if buffer.lower() != 's':
                self.itens.remove(item)
        codigo = ''
        print("Novos itens:")
        while True:
            codigo = input(f"Código do Calcado: (deixe em branco para parar)\n")
            if codigo == '':
                break
            quantidade = input(f"Quantidade do produto vendido:\n")
            for produto in bd['3']:
                if produto.getKey() == codigo:
                    item = ItemVenda().setProduto(produto).setQuantidade(quantidade)
                    self.itens.append(item)

    def getKey(self):
        return str(self.numero)

    def total(self):
        sum = 0
        for item in self.itens:
            sum += item.total()
        return sum
            