#Exercicio 2
#Sistema de cadastro de pacientes
#1-Cadastrar paciente
#2-Mostrar paciente cadastrado
#3-Atender paciente
#4-Sair
def menu():
    print("\n--- Bilheteria de Evento ---")
    print ("1- Cadastrar nome do evento")
    print("2- Vender ingressos")
    print("3- Repor ingressos")
    print("4- Ver ingressos disponíveis")
    print("0- Sair")
    return input ("Escolha uma opção: ")

while True:
    opcao = menu()
    if opcao == "1":
        evento = input("Digite o nome do evento")
        quantidade_de_ingressos = 1200
        print (f"Nome do evento cadastrado com sucesso")
        
    elif opcao == "2":
        venda = int(input("Quantos você quer vender: "))
     
    elif opcao == "3":
        if evento is None:
            print("Nenhum evento cadastrado ainda!")
        else: 
            repor = int(input("Digite a quantidade a repor:"))
        if repor <=0:
            print ("A quantidade deve ser maior que zero!")
        else:
            quantidade += repor
            print(f"Adicionado {repor} ingresso(s). Estoque atual: {quantidade}")
                     
    elif opcao =="4":
        if evento is None:
            print("Nenhum Evento cadastrado ainda!")
        else:
            print(f"Evento: {evento} | Quantidade de ingressos em estoque: {quantidade}")
    elif opcao == "0":
         print("Saindo do sistema... até mais!")
         break
                 
    else:
        print("Opção inválida! Tente novamente.")
                     
               
