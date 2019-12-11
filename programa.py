import sqlite3

def conectar():
    #Funcao para conectar ao banco de dados
    conn = sqlite3.connect('psqlite3.geek')

    conn.execute(""" CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL); """
    )
    return conn


def desconectar(conn):
    #Funcao para desconectar ao banco de dados
    conn.close()

def listar():
    #Funcao para listar os proditos
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos:')
        print('------------------')
        for produto in produtos:
            print('ID: {produto[0]}')
            print('Produto: {produto[1]}')
            print('Preco: {produto[2]}')
            print('Estoque: {produto[3]}')
            print('-----------------')
    else:
        print('Nao existem produtos cadastrados.')
        desconectar(conn)

def inserir():
    #Funcao para inserir um prodito
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preco do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', '{preco}', '{estoque}')")
    conn.commit()

    if cursor.rowcount == 1:
        print('O produto {nome} foi inserido com sucesso;')
    else:
        print('Nao foi possivel inserir o produto.')
    desconectar(conn)

def atualizar():
    #Funcao para atualizar um prodito
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preco do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute("UPDATE produtos SET nome='{nome}', preco='{preco}', estoque='{estoque}' WHERE id='{codigo}")
    conn.commit

    if cursosr.rowcount == 1:
        orint('O produto {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)

def deletar():
    #Funcao para deletar um Produto
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o codigo do produto: '))
    cursor.execute("DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto excluido com sucesso.')
    else:
        print('Erro ao excluir o produto.')
    desconectar(conn)

def menu():
    #Funcao para gerar o menu inicial
    print('== Gerenciamento de Produtos ==')
    print('Selecione uma opcao:')
    print('1 - Listar produtos')
    print('2 - Inserir produtos')
    print('3 - Atualizar produtos')
    print('4 - Deletar produtos')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opcao invalida')
    else:
        print('Opcao invalida')
