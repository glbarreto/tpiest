from .Totalizavel import Totalizavel
from .Calcado import Calcado

class ItemVenda(Totalizavel):
    def __init__(self):
        super().__init__()
        self.calcado = Calcado()
        self.valor = 0.0
        self.quantidade = 0

    def setProduto(self, calcado):
        self.calcado = calcado
        self.valor = self.calcado.getValor()
        return self
    
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
        return self

    def getNome(self):
        return self.calcado.getNome()

    def getQuantidade(self):
        return self.quantidade