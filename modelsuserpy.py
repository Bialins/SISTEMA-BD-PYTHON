import bcrypt
from configpy import conectar

def cadastrar_usuario(nome, cpf, endereco, telefone, usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
   
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    query = "INSERT INTO usuario (nome, cpf, endereco, telefone, usuario, senha) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nome, cpf, endereco, telefone, usuario, hashed_senha)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Usuário {usuario} cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "SELECT id, nome, cpf, endereco, telefone, usuario from usuario"
    cursor.execute(query)
    
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    
    cursor.close()
    conexao.close()

def listar_vendas_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    SELECT u.nome AS usuario_nome, c.nome AS cliente_nome, v.nome AS vendedor_nome, p.nome AS produto_nome, vnd.quantidade, vnd.data_venda
    FROM venda vnd
    INNER JOIN usuario u ON u.id = vnd.id_usuario
    INNER JOIN cliente c ON c.id = vnd.id_cliente
    INNER JOIN vendedor v ON v.id = vnd.id_vendedor
    INNER JOIN produto p ON p.id = vnd.id_produto
    WHERE u.nome LIKE %s
    """
    cursor.execute(query, ('%Carlos%',))  
    
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)
    
    cursor.close()
    conexao.close()

def atualizar_usuario(id_usuario, nome, cpf, endereco, telefone, usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    query = "UPDATE usuario SET nome = %s, cpf = %s, endereco = %s, telefone = %s, usuario = %s, senha = %s WHERE id = %s"
    valores = (nome, cpf, endereco, telefone, usuario, hashed_senha, id_usuario)
    
    cursor.execute(query, valores)
    conexao.commit()
    
    print(f"Usuário com ID {id_usuario} atualizado com sucesso!")
    cursor.close()
    conexao.close()

def deletar_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "DELETE FROM usuario WHERE id = %s"
    cursor.execute(query, (id_usuario,))
    conexao.commit()
    
    print(f"Usuário com ID {id_usuario} deletado com sucesso!")
    cursor.close()
    conexao.close()


def login_usuario(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    query = "SELECT id, usuario, senha FROM usuario WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    
    usuario_db = cursor.fetchone()
    
    if usuario_db:
       
        if bcrypt.checkpw(senha.encode('utf-8'), usuario_db[2].encode('utf-8')):
            print(f"Login bem-sucedido! Bem-vindo, {usuario_db[1]}")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")
    
    cursor.close()
    conexao.close()
