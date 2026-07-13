print("================================")
print("Sistema de Controle de Estoque")
print("================================")


produtos = []


while True:

    print("\nMenu:")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Alterar Produto")
    print("5 - Excluir Produto")
    print("0 - Sair")


    opcao = input("Escolha uma opção: ")


    if opcao == "1":

        print("\n--- Cadastro de Produto ---")

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade: "))


        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }


        produtos.append(produto)


        print("\nProduto cadastrado com sucesso!")
        print(produto)



    elif opcao == "2":

        print("\n--- Lista de Produtos ---")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")

        else:
            for produto in produtos:
                print("----------------")
                print("Nome:", produto["nome"])
                print("Preço:", produto["preco"])
                print("Quantidade:", produto["quantidade"])



    elif opcao == "3":
        print("Você escolheu buscar produto")


    elif opcao == "4":
        print("Você escolheu alterar produto")


    elif opcao == "5":
        print("Você escolheu excluir produto")


    elif opcao == "0":
        print("Sistema encerrado!")
        break


    else:
        print("Opção inválida!")