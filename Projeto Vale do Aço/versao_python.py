import pandas as pd

dados = []

def adicionar_dados():
    empresa = input("Empresa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    padrao = input("Padrão: ")
    motor = input("Motor: ")
    cambio = input("Câmbio: ")
    ano = input("Ano: ")
    num_veiculo = input("N° Veiculo: ")

    novo_dado = {
        'Empresa': empresa,
        'Marca': marca,
        'Modelo': modelo,
        'Padrão': padrao,
        'Motor': motor,
        'Câmbio': cambio,
        'Ano': ano,
        'N° Veiculo': num_veiculo
    }

    dados.append(novo_dado)
    print("Dados adicionados com sucesso.")

def remover_dados():
    num_veiculo = input("Digite o N° Veiculo a ser removido: ")

    for dado in dados:
        if dado['N° Veiculo'] == num_veiculo:
            dados.remove(dado)
            print("Dados removidos com sucesso.")
            return

    print("N° Veiculo não encontrado.")

def exibir_dados():
    if not dados:
        print("Nenhum dado cadastrado.")
        return

    df = pd.DataFrame(dados)
    print(df)

while True:
    print("\n1. Adicionar Dados")
    print("2. Remover Dados")
    print("3. Exibir Dados")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_dados()
    elif opcao == '2':
        remover_dados()
    elif opcao == '3':
        exibir_dados()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")