

#Dia 02:Agora vamos aprender a usar condicionais para verificar se certos 
# produtos estão no estoque e gerenciar quantidades.

#Desafio 1: Verificar se um produto específico está no estoque. 
# (Procurar na lista já criada no dia anterior)

from Dia01 import estoque

if "Caneta" in estoque:
    print("Item está no estoque.")
else:
    print("Item nao está no estoque.")

if "Tesoura" in estoque:
    print("Item está no estoque.")
else:
    print("Item nao está no estoque.")

#Desafio 2: Criar um dicionário para armazenar a quantidade de cada produto. 
# Atualizar o dicionário com valores fictícios.

dict_estoque = {'Lápis': 0, 'Apontador': 6, 'Borracha': 30, 
                'Tesoura': 7, 'Papel': 10, 'Régua': 20, 
                'Marcador': 5, 'Caderno': 15, 'Mochila': 5, 
                'Quadro-negro': 2, 'Piloto': 12}




#Desafio 3: Se o produto "Maçã" estiver no estoque, 
# reduza sua quantidade em 2 (simulando a venda de 2 unidades).
# Criar um dicionário para armazenar a quantidade de cada produto. 
# Atualizar o dicionário com valores fictícios se produto 
# específico está no estoque.


produto = input("Informe o produto que deseja vender: ")
quant_item = 2

if produto in dict_estoque:
    dict_estoque[produto] -= 2 

else:
    print("Produto não disponivel em estoque.")

print(dict_estoque)