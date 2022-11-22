class Menu(object):
    def main(self):
        print(f"\n--Menu--")
        print("1. Venda")
        print("2. Cliente")
        print("3. Produto")
        print("4. Sair")
    
    def entity(self, entity):
        print(f"--{entity}--")
        print(f"1. Cadastrar")
        print(f"2. Listar")
        print(f"3. Alterar")
        print(f"4. Deletar")
        print(f"5. Voltar")
