import bcrypt
from configpy import conectar

def cadastrar_cliente(nome, cpf, endereco, telefone, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    query = "INSERT INTO cliente (nome, cpf, endereco, telefone, senha) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, cpf, endereco, telefone, hashed_senha)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Cliente {nome} cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "SELECT id, nome, cpf, endereco, telefone from cliente"
    cursor.execute(query)
    
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    
    cursor.close()
    conexao.close()

def listar_vendas_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    SELECT c.nome AS cliente_nome, v.nome AS vendedor_nome, p.nome AS produto_nome, vnd.quantidade, vnd.data_venda
    FROM venda vnd
    INNER JOIN cliente c ON c.id = vnd.id_cliente
    INNER JOIN vendedor v ON v.id = vnd.id_vendedor
    INNER JOIN produto p ON p.id = vnd.id_produto
    WHERE c.nome LIKE %s
    """
    cursor.execute(query, ('%Maria%',)) 
    
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)
    
    cursor.close()
    conexao.close()

def atualizar_cliente(id_cliente, nome, cpf, endereco, telefone, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    query = "UPDATE cliente SET nome = %s, cpf = %s, endereco = %s, telefone = %s, senha = %s WHERE id = %s"
    valores = (nome, cpf, endereco, telefone, hashed_senha, id_cliente)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Cliente com ID {id_cliente} atualizado com sucesso!")
    cursor.close()
    conexao.close()

def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "DELETE FROM cliente WHERE id = %s"
    cursor.execute(query, (id_cliente,))
    conexao.commit()
    
    print(f"Cliente com ID {id_cliente} deletado com sucesso!")
    cursor.close()
    conexao.close()
