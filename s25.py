Estoque = [20, 15, 10, 30, 5]
def atualizar(elemento, quantidade):
    posicao = elemento - 1
    Estoque[posicao]-= quantidade
    