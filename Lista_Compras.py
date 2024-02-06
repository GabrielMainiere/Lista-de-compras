"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista. Não permita que o programa quebra com erros de índices inexistentes na lista
"""
print('Lista de Compras')
lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir | [a]pagar | [l]istar: ')

    if opcao.lower() == 'i':
        item = input('Digite o item a ser inserido: ')
        lista.append(item)

    elif opcao.lower() == 'a':
        try:
            indice_apagar = int(input('Digite o índice do item que você deseja apagar: '))
            if indice_apagar >= 0 and indice_apagar <= len(lista):
                lista.pop(indice_apagar)
            else:
                print('Índice inválido.')
        except ValueError:
            print('Índice inválido.')
            continue

    elif opcao.lower() == 'l':
        for indice, item_listado in enumerate(lista):
            print(indice,"|",item_listado)
            

    else:
        print('Opção inválida.')
        continue
    