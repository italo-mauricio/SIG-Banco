from cadacliente import *

dici = diciclientes

dicicaixa = {}
def deposibanco():
     print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao depósito! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu depósito! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)



def saquebanco():
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao saque! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu saque! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        cadastro = input("Digite a sua senha: ")
        if cadastro not in dici:
            print("Usuário não encontrado!")
            break
        else:
            print("Cliente encontrado!")
            valor = int(input('Qual o valor você quer sacar da sua conta: '))
            cedula = 50
            total = valor
            cedt = 0
            while True:
                if total >= cedula:
                    total -= cedula
                    cedt +=1
                else:
                    print(f'Total de {cedt} céduas de R${cedula}')
                    if cedula == 50:
                        cedula = 20
                    elif cedula == 20:
                        cedula = 10
                    elif cedula == 10:
                        cedula = 1
                    cedt = 0
                    if total == 0:
                        break
      
