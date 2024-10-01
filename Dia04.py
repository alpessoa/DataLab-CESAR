#Dia 4: Funções para gerenciamento.
estoque = {}

#Desafio 1: Criar uma função chamada adicionar_produto() 
#que recebe o nome de um produto e a quantidade e o adiciona ao estoque
#(A função deve adicionar a um dicionario chamado estoque).

def adicionar_produto(produto, quantidade):
     estoque[produto] = quantidade
     return f"{quantidade} {produto} foi adicionado ao estoque."

#Desafio 2: Criar uma função remover_produto() que remove um 
#produto do estoque e do dicionário de quantidades 
#( a função deve remover do dicionario chamado estoque)
def remover_produto(produto):
     if produto in estoque:
          del estoque[produto]
          return f"{produto} foi removido do estoque."
     else:
        return f"Não possui o produto {produto} no estoque"
     

print(adicionar_produto("Banana",5))
print(remover_produto("Maçã"))
print(estoque)
     
