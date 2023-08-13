def menu():
    menu = -1
    #Será realizado o loop até o consumidor inserir um valor válido;
    while menu < 1 or menu > 8:
        menu = int(input("""\t\tFavor, digite a operação: 
                
                (1)\tSACAR
                (2)\tDEPOSITAR 
                (3)\tVISUALIZAR EXTRATO,
                (4)\tCRIAR USUARIO
                (5)\tCRIAR CONTA
                (6)\tLISTAR CONTA  
                (7)\tSAIR \n                               
                """))

        if menu <1 or menu > 8:
            print("Operação inválida, tente novamente!\n\n") 

    return (menu)
def saque(*,saldo, valor_saque, extrato, limite, saques_diarios):
    #Verificação se há saques disponíveis a ser realizado no dia.
    if saques_diarios <=0:
        print("Limite de 3 saques diários atingidos, tente outro dia")

    #Verificação valor limite de saque
    elif (valor_saque > limite or valor_saque <= 0):
        print("Operação inválida.\n")


        #Verificação de saldo na conta
    elif (valor_saque > saldo):     
        print("Saldo indisponível.\n")      
        
        
    else:
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        saldo -= valor_saque
        saques_diarios -= 1

        print(f"Saque de R$ {valor_saque:.2f} realizado.")

    return saldo,extrato, saques_diarios

def deposito(saldo, valor_deposito, extrato, /):

    if (valor_deposito <= 0):

        print("Valor incorreto, tente novamente.\n")

    else:
                    
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        saldo += valor_deposito
        
        print(f'Depósito de R${valor_deposito:.2f} realizado.\n')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações\n\n" if not extrato else f'=========Extrato:=========\n{extrato}\n' )
    print(f'Saldo atual: R${saldo:.2f}\n\n')

def criar_usuario(usuarios):
    cpf = str(input("Infome o CPF (somente numeros, sem caracteres especiais):\n"))
    usuario = filtrar_usuario(cpf, usuarios)


    if usuario:
        print(f"CPF {cpf} já cadastrado\n")

    else:
        nome = str(input("Digite o nome completo:\n"))
        data_nascimento = str(input("Digite a data de nascimento (dd/mm/aaaa):\n"))
        endereco = str(input("Digite o endereço (logradouro, nº - bairro - cidade/sigla do estado):\n"))

        usuarios.append({"cpf":cpf, "Nome":nome, "Data de nascimento":data_nascimento, "Endereço":endereco})
        print("Usuário criado com sucesso.")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    filtro_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro_usuario[0] if filtro_usuario else None
     
def criar_conta(agencia, numero_conta, usuarios, contas):
    
    cpf = str(input("Infome o CPF (somente numeros, sem caracteres especiais):\n"))

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:

        print("Conta criada com sucesso.\n")
        conta = {"Agência":agencia, "Numero da conta": numero_conta, "Usuário": usuario }
        contas.append(conta)
        return contas
    else:

        print("CPF não cadastrado.\n")

def listar_contas(contas):
        for conta in contas:

            print(f"""
                  Agência:{conta["Agência"]}
                  C\C:{conta['Numero da conta']}
                  Titular:{conta["Usuário"]["Nome"]}
                  """)
            
def main():
    import sys

    saques_diarios = 3
    agencia = "0001"

    
    limite = 500
    saldo = 0
    extrato = ""    
    usuarios = [] 
    contas = []   


    while True:

        operacao = menu()

        if operacao == 1: #Função Sacar
            valor_saque = float(input("Informe o valor a ser sacado.\n"))

          
            saldo, extrato, saques_diarios = saque(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite=limite,
                saques_diarios =saques_diarios)

        elif operacao == 2: #Função depositar
            
            valor_deposito = float(input("Informe o valor do depósito\n"))
            

            saldo, extrato = deposito(saldo,valor_deposito,extrato) 

        elif operacao == 3: #Função visualizar extrato
            exibir_extrato(saldo, extrato = extrato)

        elif operacao == 4: #Função novo usuario
            criar_usuario(usuarios)

        elif operacao == 5: #Função Criar conta 
            numero_conta = len(contas) + 1 
            criar_conta(agencia, numero_conta, usuarios, contas)            
            
        elif operacao == 6: #Função Listar contas
            listar_contas(contas)
        elif operacao == 7:
            print("Finalizando a operação.")
            sys.exit() #finaliza o sistema quando o código 4 é acionado 

        
main()