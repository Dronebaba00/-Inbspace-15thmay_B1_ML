#### Log in #######
A= input('Do you want to register (Yes/No):')

UP=LO=DI=0

if A=='Yes':
    Userid=input('Enter User Name :-')
    pwd= input('Enter the password :-')
    for i in pwd:
        if i.isdigit():
            DI =DI+1
        if i.islower():
            LO  = LO+1
        if i.isupper():
            UP =UP+1
    if UP>0 and LO>0 and DI>0:
        UI= input("Enter the User name :-")
        pw=input("Enter the Password :-")
        if UI==Userid and pw==pwd:
            print("Welcom")
            Option=input("1. Basic Calculator 2. Table Generator 3. Pattern Generator")
            if Option == '1':
                V1=int(eval(input("Enter Value 1:-")))
                V2=int(eval(input("Enter Value 2:-")))
                Oper= input("1. Addidtion 2. Subtraction 3. Multiplication 4. Division")
                if Oper=='1':
                    Add=V1+V2
                    print("Addition is:",Add)
                if Oper == '2':
                    Sub=V1-V2
                    print("Subtraction is:",Sub)
                if Oper == '3':
                    Mul= V1*V2
                    print("Multiplication is:",Mul)
                if Oper == '4':
                    Div= V1/V2
                    print("Division is:",Div)
            if Option == '2':
                Baba=int(eval(input('Enter a value:')))
                for l in range(1, 11):
                    print(Baba, 'x', l, '=', Baba*l)
            if Option =='3':
                Row=int(eval(input('Enter a row:-')))
                for ra in range(1, Row+1):
                    for ca in range(1, ra+ 1):
                        print(ca, end="")
                    print('\r')                       
                   
    else :
        print("Not Valid - Capital , numerical etc")
        
else :
    print('Bye')

