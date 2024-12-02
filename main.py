import getpass
from modelsclientespy import cadastrar_cliente, listar_clientes, atualizar_cliente, deletar_cliente
from modelsvendedorespy import cadastrar_vendedor, listar_vendedores, atualizar_vendedor, deletar_vendedor
from modelsprodutospy import cadastrar_produto, listar_produtos, listar_vendas_produtos, atualizar_produto, deletar_produto
from modelsuserpy import cadastrar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario, login_usuario

def menu():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Gerenciar Clientes")
        print("4. Gerenciar Vendedores")
        print("5. Login")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            menu_clientes()
        elif opcao == "4":
            menu_vendedores()
        elif opcao == "5":
            login()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def login():
    usuario = input("Digite o usuário: ")
    senha = getpass.getpass("Digite a senha: ")
    sucesso = login_usuario(usuario, senha)
    if sucesso:
        print("Login bem-sucedido!")
    else:
        print("")

def menu_usuarios():
    while True:
        print("\nGerenciamento de Usuários:")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            cpf = input("CPF do usuário: ")
            endereco = input("Endereço do usuário: ")
            telefone = input("Telefone do usuário: ")
            usuario = input("Usuário: ")
            senha = getpass.getpass("Senha: ")
            cadastrar_usuario(nome, cpf, endereco, telefone, usuario, senha)
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            id_usuario = int(input("ID do usuário a ser atualizado: "))
            nome = input("Novo nome: ")
            cpf = input("Novo CPF: ")
            endereco = input("Novo endereço: ")
            telefone = input("Novo telefone: ")
            usuario = input("Novo usuário: ")
            senha = input("Nova senha: ")
            atualizar_usuario(id_usuario, nome, cpf, endereco, telefone, usuario, senha)
        elif opcao == "4":
            id_usuario = int(input("ID do usuário a ser deletado: "))
            deletar_usuario(id_usuario)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produtos():
    while True:
        print("\nGerenciamento de Produtos:")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Listar Vendas de Produtos")
        print("4. Atualizar Produto")
        print("5. Deletar Produto")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            cadastrar_produto(nome, preco, quantidade)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            listar_vendas_produtos()
        elif opcao == "4":
            id_produto = int(input("ID do produto a ser atualizado: "))
            nome = input("Novo nome: ")
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade: "))
            atualizar_produto(id_produto, nome, preco, quantidade)
        elif opcao == "5":
            id_produto = int(input("ID do produto a ser deletado: "))
            deletar_produto(id_produto)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_clientes():
    while True:
        print("\nGerenciamento de Clientes:")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            endereco = input("Endereço do cliente: ")
            telefone = input("Telefone do cliente: ")
            senha = getpass.getpass("Digite a senha: ")
            cadastrar_cliente(nome, cpf, endereco, telefone, senha)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            id_cliente = int(input("ID do cliente a ser atualizado: "))
            nome = input("Novo nome: ")
            cpf = input("Novo CPF: ")
            endereco = input("Novo endereço: ")
            telefone = input("Novo telefone: ")
            senha = input("Nova Senha: ")
            atualizar_cliente(id_cliente, nome, cpf, endereco, telefone, senha)
        elif opcao == "4":
            id_cliente = int(input("ID do cliente a ser deletado: "))
            deletar_cliente(id_cliente)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_vendedores():
    while True:
        print("\nGerenciamento de Vendedores:")
        print("1. Cadastrar Vendedor")
        print("2. Listar Vendedores")
        print("3. Atualizar Vendedor")
        print("4. Deletar Vendedor")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do vendedor: ")
            cpf = input("CPF do vendedor: ")
            endereco = input("Endereço do vendedor: ")
            telefone = input("Telefone do vendedor: ")
            senha = getpass.getpass("Senha: ")
            cadastrar_vendedor(nome, cpf, endereco, telefone, senha)
        elif opcao == "2":
            listar_vendedores()
        elif opcao == "3":
            id_vendedor = int(input("ID do vendedor a ser atualizado: "))
            nome = input("Novo nome: ")
            cpf = input("Novo CPF: ")
            endereco = input("Novo endereço: ")
            telefone = input("Novo telefone: ")
            senha = getpass.getpass("Nova senha: ")
            atualizar_vendedor(id_vendedor, nome, cpf, endereco, telefone, senha)
        elif opcao == "4":
            id_vendedor = int(input("ID do vendedor a ser deletado: "))
            deletar_vendedor(id_vendedor)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
