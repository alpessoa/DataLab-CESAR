#Dia 3: Loops e atualização automatica.

#Desafio 1:Percorrer a lista do estoque, usando um for,  
#e exibir cada produto!

from Dia01 import estoque
from Dia02 import dict_estoque, produto

for item in estoque:
    print(item)


#Desafio 2: Criar um loop que permita ao usuário reduzir a quantidade
#de um produto até que ele fique sem estoque.

while dict_estoque[produto] > 0:
    quantidade_venda = int(input(f'''Quantas unidades de {produto} você deseja
                                  vender? 
                                 (Disponível: {dict_estoque[produto]}): '''))
    if quantidade_venda > 0 and quantidade_venda <= dict_estoque[produto]:
        dict_estoque[produto] -= quantidade_venda
        print(f"Vendidas {quantidade_venda} unidades de {produto}.")
    else:
        print("Quantidade inválida ou insuficiente.")

print(f"{produto} está esgotado.")

