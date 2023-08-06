saques_diarios = 3
saldo = 0
extrato = [saldo]


def operacoes_bancarias():
    operacao = -1 # variavel adicionada para fazer o loop das operações quando digitado um número inválido
    valor_deposito = 0
    valor_saque = 0
    global saques_diarios
    global extrato
    global saldo
    import sys

    
    

    #Será realizado o loop até o consumidor inserir um valor válido;
    while operacao <= 0 or operacao > 4:
        operacao = int(input("""Favor, digite a operação: 
                
                (1) SACAR
                (2) DEPOSITAR 
                (3) VISUALIZAR EXTRATO
                (4) SAIR
                
                """))

        if operacao <=0 or operacao > 4:
            print("Operação inválida, tente novamente!")    


    # Operação SACAR

    if operacao == 1:

        #Verificação se há saques disponíveis a ser realizado no dia.
        if saques_diarios <=0:
            print("Limite de 3 saques diários atingidos, tente outro dia")

        else:


            #Loop para permitir somente valores maiores que R$0 e no máximo R$500.
            while (valor_saque > 500 or valor_saque <= 0):
            
                valor_saque = int(input("Favor, digite o valor a ser sacado:\n"))
                
                if (valor_saque > 500 or valor_saque <= 0):
                    print("Operação inválida, tente novamente\n\n")
                
                
                    
            #Verificação de saldo na conta
            if valor_saque > saldo:        
                print("Saldo indisponível.")

            else:
                extrato.append(-valor_saque)
                saldo -= valor_saque
                saques_diarios -= 1

                print(f"Saque de R${valor_saque:.2f} realizado, seu saldo disponível é R${saldo:.2f}")
            

    # Operação DEPOSITAR
    elif operacao == 2:
        while (valor_deposito <= 0):
        
            valor_deposito = int(input("Digite o valor a ser depositado:\n"))


            if valor_deposito <=0:
                print("Valor incorreto, tente novamente.\n")
        extrato.append(valor_deposito)
        saldo += valor_deposito
        print(f'Depósito de R${valor_deposito:.2f} realizado, o seu saldo atual é de {saldo:.2f}')

        
    # Operação VISUALIZAR EXTRATO
    elif operacao == 3:

        if not extrato:
            print("Não foram realizadas movimentações\n\n")
        else:
            print(extrato)
            print(f'Saldo atual: R${saldo:.2f}\n\n')

    # Operação SAIR
    elif operacao == 4:
        print("Finalizando a operação.")
        sys.exit() #finaliza o sistema quando o código 4 é acionado





while True:
    operacoes_bancarias()








