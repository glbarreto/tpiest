from ..Model.Venda import Venda
from ..Model.Cliente import Cliente
from ..Model.Calcado import Calcado
from ..View.Menu import Menu

class MenuController(object):

    def __init__(self):
        self.bd = {
            '1': [],
            '2': [],
            '3': []
        }

    def show(self):
        menu = Menu()      
        while True:
            try:
                menu.main()
                self.entity = input()
                while True:
                    menu.entity(self.strEntity())
                    self.action = input()
                    self.entityClass = self.switchClass()
                    self.switchAction()
            except Exception as e :
                if e.args[0] == 1:
                    break
                elif e.args[0] == 2:
                    continue
                else:
                    raise e


    def strEntity(self):
        if(self.entity == '1'):
            return 'Venda'
        elif(self.entity == '2'):
            return 'Cliente'
        elif(self.entity == '3'):
            return 'Produto'
        else:
            raise Exception(1)

    def switchClass(self):
        if(self.entity == '1'):
            return Venda()
        elif(self.entity == '2'):
            return Cliente()
        elif(self.entity == '3'):
            return Calcado()
        else:
            raise Exception(2)

    def switchAction(self):
        if(self.action == '1'):
            self.entityClass.setAll(self.bd)
            self.bd[self.entity].append(self.entityClass)
        elif(self.action == '2'):
            print(f'--{self.strEntity()}s--')
            for entity in self.bd[self.entity]:
                print(entity.toString())
        elif(self.action == '3'):
            self.printKey()
            key = input()
            notFound = True
            for entity in self.bd[self.entity]:
                if(entity.getKey() == key):
                    notFound = False
                    self.entityClass = entity
                    break
            if(notFound):
                print(f"{self.strEntity()} não existe.")
                return
            self.entityClass.alter(self.bd)
            for entity in self.bd[self.entity]:
                if(entity.getKey() == key):
                    entity = self.entityClass
                    break
            print("Alterações salvas com sucesso.")
        elif(self.action == '4'):
            self.printKey()
            key = input()
            notFound = True
            for entity in self.bd[self.entity]:
                if(entity.getKey() == key):
                    notFound = False
                    self.entityClass = entity
                    break
            if(notFound):
                print(f"{self.strEntity()} não existe.")
                return
            self.bd[self.entity].remove(self.entityClass)
            print(f"Exclusão bem sucedida.")
        else:
            raise Exception(2)

    def printKey(self):
        if(self.entity == '1'):
            print('Digite o número da Venda:')
        elif(self.entity == '2'):
            print('Digite o RG do Cliente:')
        else:
            print('Digite o Código do Produto')