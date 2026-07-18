
i = 1
while i == True:

    calcular = input("vc quer continuar?: ").lower()
    if calcular in ["não", "nao", "Não", "nn", "NN","Nao", "NAO","not","no","n"]:
        continue

    else :
        i = 1

    numero1 = input("digite um número:")
    operador = input("digite o operador (só pode ser '+,-,*,/)")
    numero2 = input("digite o segundo número:")
    
    try: #atenção
        numero1float = float(numero1) 
        numero2float = float(numero2)
    except: #atenção
        print("DIGITE UM NÚMERO VÁLIDO")
        continue


    if operador == "+" :
            print(numero1float + numero2float)

    elif operador == "-":
            print(numero1float - numero2float)

    elif operador == "*":
            print(numero1float * numero2float)

    elif operador == "/":
            print(numero1float / numero2float)        

    else:
        print("DIGITE O OPERADOR CORRETO")
        continue
    
    continue
