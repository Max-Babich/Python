def CranesAmount(total):
    
    x = total // 6
    print(f' Petya made {x} \n Sergey made {x} \n Katya made {4*x}')


amount = int(input("Please, set total amount of Cranes were made = "))
CranesAmount(amount)