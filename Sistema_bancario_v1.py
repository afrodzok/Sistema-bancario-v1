from time import sleep

menu = 0 
saldo = 0
numero_saque = 0
extrato_deposito = list()
extrato_saque = list()
while menu != 4:
    print("""
=========================================
Seja bem vindo!!
Informe a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
""")
    menu = int(input("=> "))
    if menu == 1:
        novo_deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if novo_deposito> 0:
            saldo = saldo + novo_deposito
            print("Deposito realizado!")
            extrato_deposito.append(novo_deposito)
            sleep(1)
        else: print ("Valor invalido")
        sleep(1)
    elif menu == 2:
        saque = float(input("Digite o valor do Saque: R$ "))
        if numero_saque >= 3:
            print("Limite de saque excedido!")
            sleep(1)
        elif saldo < saque:
            print("Saldo insuficiente")
            sleep(1) 
        elif saque < 0:
            print("Valor informado não é valido.")     
            sleep(1)       
        elif saque <= 500 and saque != 0:
            saldo = saldo - saque
            numero_saque = numero_saque + 1
            print("Saque realizado!")
            extrato_saque.append(saque)
            sleep(1)
        else: print ("Valor de minimo de saque excedido!")
        sleep(1)            
    elif menu == 3:
        if extrato_deposito != []:
            print("========================================")  
            for D in extrato_deposito:
                print(f"Depositos: R$ +{D}")
            print("========================================")  
            for S in extrato_saque:
                print(f"Saques: R$ -{S}")
            print("========================================")    
            print("Saldo da Conta R$",saldo)
            sleep(1)
        else: 
            print("Não foram realizadas movimentações.")
            sleep(1)      
    elif menu == 4:
        print ("Finalizando programação......")
        sleep(0.5)
print ("Volte sempre!")
sleep(2)