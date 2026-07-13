from arquivo import carregar_produtos, salvar_produtos

print("================================")
print("Sistema de Controle de Estoque")
print("================================")

produtos = carregar_produtos()

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

        while True:
            try:
                preco = float(input("Digite o preço do produto: "))
                break
            except ValueError:
                print("Preço inválido! Digite apenas números.")

        while True:
            try:
                quantidade = int(input("Digite a quantidade: "))
                break
            except ValueError:
                print("Quantidade inválida! Digite apenas números inteiros.")


        # Criando ID automático
        if len(produtos) == 0:
            novo_id = 1
        else:
            novo_id = max(produto.get("id", 0) for produto in produtos) + 1


        produto = {
            "id": novo_id,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }


        produtos.append(produto)

        salvar_produtos(produtos)


        print("\nProduto cadastrado com sucesso!")
        print(produto)


    elif opcao == "2":

        print("\n--- Lista de Produtos ---")


        if len(produtos) == 0:

            print("Nenhum produto cadastrado.")

        else:

            for produto in produtos:

                print("----------------")
                print("ID:", produto.get("id", "Sem ID"))
                print("Nome:", produto["nome"])
                print("Preço:", produto["preco"])
                print("Quantidade:", produto["quantidade"])



    elif opcao == "3":

        print("\n--- Buscar Produto ---")

        nome_busca = input("Digite o nome do produto: ")

        encontrado = False


        for produto in produtos:

            if produto["nome"].lower() == nome_busca.lower():

                print("\nProduto encontrado!")
                print("----------------")
                print("ID:", produto.get("id", "Sem ID"))
                print("Nome:", produto["nome"])
                print("Preço:", produto["preco"])
                print("Quantidade:", produto["quantidade"])

                encontrado = True
                break


        if not encontrado:

            print("Produto não encontrado.")



    elif opcao == "4":

        print("\n--- Alterar Produto ---")

        nome_alterar = input("Digite o nome do produto que deseja alterar: ")

        encontrado = False


        for produto in produtos:

            if produto["nome"].lower() == nome_alterar.lower():

                print("\nProduto encontrado!")


                novo_preco = float(input("Digite o novo preço: "))
                nova_quantidade = int(input("Digite a nova quantidade: "))


                produto["preco"] = novo_preco
                produto["quantidade"] = nova_quantidade


                salvar_produtos(produtos)


                print("\nProduto alterado com sucesso!")

                encontrado = True
                break


        if not encontrado:

            print("Produto não encontrado.")



    elif opcao == "5":

        print("\n--- Excluir Produto ---")


        nome_excluir = input("Digite o nome do produto que deseja excluir: ")

        encontrado = False


        for produto in produtos:

            if produto["nome"].lower() == nome_excluir.lower():

                produtos.remove(produto)

                salvar_produtos(produtos)


                print("\nProduto excluído com sucesso!")

                encontrado = True
                break


        if not encontrado:

            print("Produto não encontrado.")



    elif opcao == "0":

        print("Sistema encerrado!")
        break



    else:

        print("Opção inválida!")