
class Calcado(object):
    def __init__(self):
        self.codigo = 0
        self.nome = ''
        self.valor = 0.0

    def getValor(self):
        return self.valor

    def getNome(self):
        return self.nome

    def toString(self):
        return f"Código: {self.codigo}\n\
Nome: {self.nome}\n\
Valor: {self.valor}\n\n"

    def setAll(self, bd):
        print("Digite os dados do calçado")
        self.codigo = int(input(f"Codigo:\n"))
        self.nome = input(f"Nome:\n")
        self.valor = float(input(f"Valor:\n"))
        

    def alter(self, bd):
        print("Digite os novos dados do calçado: (deixe em branco para não alterar)")
        buffer = input(f"Codigo:\n")
        if buffer != '':
            self.codigo = int(buffer)
        buffer = input(f"Nome:\n")
        if buffer != '':
            self.nome = buffer
        buffer = input(f"Valor:\n")
        if buffer != '':
            self.valor = float(buffer)

    def getKey(self):
        return str(self.codigo)