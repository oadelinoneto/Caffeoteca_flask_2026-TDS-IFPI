listaProdutos = []

class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco


    def adicionar_produto(id, nome, descricao, preco):
        produto = Produto(id, nome, descricao, preco)
        listaProdutos.append(produto)
  

  # nome
  #descricao
  #preco