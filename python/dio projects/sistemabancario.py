menu = """

[1] Sacar dinheiro
[2] Depositar dinheiro
[3] Extrato bancário
[0] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "2":
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito efetuado no valor de R$ {valor:.2f} com sucesso!\n")
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Falha! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print(f"Falha! O valor do saque excede o limite. Seu limite por saque é de R$ {limite:.2f}\n")
        
        elif excedeu_saques:
            print(f"Falha! O número máximo de {LIMITE_SAQUES} saques diários excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso!\n")
            
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "3":
        print("\n================ EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == 0:
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        