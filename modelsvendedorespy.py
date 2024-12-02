import bcrypt
from configpy import conectar

def cadastrar_vendedor(nome, cpf, endereco, telefone, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    query = "INSERT INTO vendedor (nome, cpf, endereco, telefone, senha) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, cpf, endereco, telefone, hashed_senha)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Vendedor {nome} cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_vendedores():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "SELECT id, nome, cpf, endereco, telefone from vendedor"
    cursor.execute(query)
    
    vendedores = cursor.fetchall()
    for vendedor in vendedores:
        print(vendedor)
    
    cursor.close()
    conexao.close()

def listar_vendas_vendedores():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    SELECT v.nome AS vendedor_nome, c.nome AS cliente_nome, p.nome AS produto_nome, vnd.quantidade, vnd.data_venda
    FROM venda vnd
    INNER JOIN vendedor v ON v.id = vnd.id_vendedor
    INNER JOIN cliente c ON c.id = vnd.id_cliente
    INNER JOIN produto p ON p.id = vnd.id_produto
    WHERE v.nome LIKE %s
    """
    cursor.execute(query, ('%João%',))  
    
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)
    
    cursor.close()
    conexao.close()

def atualizar_vendedor(id_vendedor, nome, cpf, endereco, telefone, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    query = "UPDATE vendedor SET nome = %s, cpf = %s, endereco = %s, telefone = %s, senha = %s WHERE id = %s"
    valores = (nome, cpf, endereco, telefone, hashed_senha, id_vendedor)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Vendedor com ID {id_vendedor} atualizado com sucesso!")
    cursor.close()
    conexao.close()

def deletar_vendedor(id_vendedor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "DELETE FROM vendedor WHERE id = %s"
    cursor.execute(query, (id_vendedor,))
    conexao.commit()
    
    print(f"Vendedor com ID {id_vendedor} deletado com sucesso!")
    cursor.close()
    conexao.close()
