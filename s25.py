estoque = [20, 15, 10, 30, 5]
def atualizar(elemento, quantidade):
    posiçao = elemento - 1
    if 0 <= posiçao < len(estoque):
        estoque[posiçao]-= quantidade
    else:
        print("Elemento inválido!")
    
def exibir (estoque):
    print(f"Estoque atual :{estoque}")

def adicionar(elemento, quatidade):
    posiçao = elemento - 1
    if 0<= posiçao < len(estoque):
        estoque[posiçao]+= quatidade
    else:
        print("Elemento Inválido")
exibir(estoque)
atualizar(1,3 )        
print("estoque atualizado")
exibir(estoque)
        
