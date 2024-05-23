
manifestacoes = []
codigo_atual = 1



while True:

    print("\nMenu do Sistema:")
    print("1) Listagem das Manifestações")
    print("2) Listagem de Manifestações por Tipo")
    print("3) Criar uma nova Manifestação")
    print("4) Exibir quantidade de manifestações")
    print("5) Pesquisar uma manifestação por código")
    print("6) Excluir uma Manifestação pelo Código")
    print("7) Sair do Sistema")

 
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        if len(manifestacoes) == 0:
            print("Não existem manifestações cadastradas.")
        else:
            print("Listagem de Manifestações:")
            for manifestacao in manifestacoes:
                print(f"Código: {manifestacao['codigo']}, Tipo: {manifestacao['tipo']}, Descrição: {manifestacao['descricao']}")

 
    elif opcao == '2':
        tipo = input("Digite o tipo de manifestação (reclamação, elogio ou sugestão): ").lower()
        filtradas = [m for m in manifestacoes if m['tipo'] == tipo]
        if len(filtradas) == 0:
            print(f"Não existem manifestações do tipo '{tipo}' cadastradas.")
        else:
            print(f"Listagem de Manifestações do tipo '{tipo}':")
            for manifestacao in filtradas:
                print(f"Código: {manifestacao['codigo']}, Tipo: {manifestacao['tipo']}, Descrição: {manifestacao['descricao']}")


    elif opcao == '3':
        tipo = input("Digite o tipo de manifestação (reclamação, elogio ou sugestão): ").lower()
        descricao = input("Digite a descrição da manifestação: ")
        nova_manifestacao = {
            'codigo': codigo_atual,
            'tipo': tipo,
            'descricao': descricao
        }
        manifestacoes.append(nova_manifestacao) 
        codigo_atual += 1 
        print("Nova manifestação criada com sucesso!")


    elif opcao == '4':
        print(f"Quantidade de manifestações: {len(manifestacoes)}")


    elif opcao == '5':
        codigo = int(input("Digite o código da manifestação: "))
        encontrada = None
        for manifestacao in manifestacoes:
            if manifestacao['codigo'] == codigo:
                encontrada = manifestacao
                break
        if encontrada:
            print(f"Manifestação encontrada: Código: {encontrada['codigo']}, Tipo: {encontrada['tipo']}, Descrição: {encontrada['descricao']}")
        else:
            print(f"Não existe manifestação com o código {codigo}.")
    elif opcao == '6':
        codigo = int(input("Digite o código da manifestação a ser excluída: "))
        index_a_remover = None
        for i, manifestacao in enumerate(manifestacoes):
            if manifestacao['codigo'] == codigo:
                index_a_remover = i
                break
        if index_a_remover is not None:
            del manifestacoes[index_a_remover]
            print("Manifestação excluída com sucesso!")
        else:
            print(f"Não existe manifestação com o código {codigo}.")


    elif opcao == '7':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
 