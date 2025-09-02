def menu():
    print("\n--- Sistema de Estoque---")
    print("1 - Cadastrar Evento")
    print("2 - Vender ingresso")
    print("3 - Repor Ingressos")
    print("4 - Ver ingressos disponíveis")
    print("0 - Sair")
    return input("Escolha uma opção: ")
    
    evento = None
    quantidade = 0
    
while True:
    
    opcao = menu()
    
    if opcao == "1":
        evento = input("Digite o nome do Evento: ")
        quantidade = 0
        print(f"Evento '{evento}' cadastrado com sucesso!")

    elif opcao == "2":
        if evento is None:
            print("Nenhum evento cadastrado ainda!")
        else:
            vender = int(input("Digite a quantidade que você quer: "))
            if vender <= 0:
                print("A quantidade deve ser maior que zero!")
            elif vender > quantidade:
                print("Quantidade insuficiente no estoque!")
            else:
                quantidade -= vender
                print(f"Vendido {vender} ingresso(s). Estoque atual: {quantidade}")

    elif opcao == "3":
        if evento is None:
            print("Nenhum evento cadastrado ainda!")
        else:
            repor = int(input("Digite a quantidade a Repor: "))
            if repor <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += repor
                print(f"Adicionado {repor} ingresso(s). Estoque atual: {quantidade}")

    elif opcao == "4":
        if evento is None:
            print("Nenhum Evento cadastrado ainda!")
        else:
            print(f"Evento: {evento} | Quantidade de ingressos em estoque: {quantidade}")

    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
    