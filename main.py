# Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente. O algoritmo deve receber o código de um produto, a quantidade comprada e calcular o preço total, usando a tabela abaixo: Código do Produto 1001, Preço Unitário 5,32, Código do Produto 1324, Preço Unitário 6,45, Código do Produto 6548, Preço Unitário 2,37, Código do Produto 987, Preço Unitário 5,32, Código do Produto 7623, Preço Unitário 6,45.

print('''Bem vindos(as) ao sistema de preços da UniRuy Wyden! 

                     Código   Preço
                    
                     1001    R$ 5.32
                     1324    R$ 6.45
                     6548    R$ 2.37
                     987     R$ 5.32
                     7623    R$ 6.45

''')
total = 0
cod = 0
valor = 0
preco = 0
while True:
  opcao = str(input('Caso deseje calcular o preço dos produtos digite p, caso deseje sair digite s: \n' ))
  if opcao == 's':
    print('Fim')
    break
  if opcao == 'p':
    cod = int(input('Digite o código do produto:\n'))
    quantidade = int(input('Digite a quantidade: \n'))
  if cod == 1001:
    a = (+5.32 * quantidade)
  elif cod == 1324:
    b = (+6.45 * quantidade)
  elif cod == 6548:
    c = (+2.37 * quantidade)
  elif cod == 987:
    d = (+5.32 * quantidade)
  elif cod == 7623:
    e = (+6.45 * quantidade)
  elif cod == 's':
    print('Fim.')
    break
  else:
    print('Código não cadastrado')
  valor = input(f'O total do pedido até o momento é de: R$ {a or b or c or d or e}')
  continue
while opcao != 's':
  input('Para continuar digite p e para sair digite s. \n')
  break 