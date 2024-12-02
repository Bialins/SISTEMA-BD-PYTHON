import bcrypt
from configpy import conectar

def cadastrar_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "INSERT INTO produto (nome, preco, quantidade) VALUES (%s, %s, %s)"
    valores = (nome, preco, quantidade)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Produto {nome} cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "SELECT * FROM produto"
    cursor.execute(query)
    
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
    
    cursor.close()
    conexao.close()

def listar_vendas_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    SELECT p.nome AS produto_nome, c.nome AS cliente_nome, v.nome AS vendedor_nome, vnd.quantidade, vnd.data_venda
    FROM venda vnd
    INNER JOIN produto p ON p.id = vnd.id_produto
    INNER JOIN cliente c ON c.id = vnd.id_cliente
    INNER JOIN vendedor v ON v.id = vnd.id_vendedor
    WHERE p.nome LIKE %s
    """
    cursor.execute(query, ('%Camiseta%',))  # Exemplo de uso do LIKE com o nome do produto contendo 'Camiseta'
    
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)
    
    cursor.close()
    conexao.close()

def atualizar_produto(id_produto, nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "UPDATE produto SET nome = %s, preco = %s, quantidade = %s WHERE id = %s"
    valores = (nome, preco, quantidade, id_produto)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Produto com ID {id_produto} atualizado com sucesso!")
    cursor.close()
    conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "DELETE FROM produto WHERE id = %s"
    cursor.execute(query, (id_produto,))
    conexao.commit()
    
    print(f"Produto com ID {id_produto} deletado com sucesso!")
    cursor.close()
    conexao.close()
