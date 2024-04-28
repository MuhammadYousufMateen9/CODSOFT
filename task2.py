def add(a,b):
    return f'\t  {a}\n\t+ {b}\n\t_________\n\033[92mAnswer :\033[0m  {a+b}\n'
def subtract(a,b):
    return f'\t  {a}\n\t- {b}\n\t_________\n\033[92mAnswer :\033[0m  {a-b}\n'
def multiply(a,b):
    return f'\t  {a}\n\tx {b}\n\t_________\n\033[92mAnswer :\033[0m  {a*b}\n'
def divide(a,b):
    return f'\t  {a}\n\t_________  =  {a/b}\n\t  {b}\n'
def calculator(a,choice,b):
    if choice==1:
       return add(a,b)
    elif choice==2:
        return subtract(a,b)
    elif choice==3:
        return multiply(a,b)
    elif choice==4:
        return divide(a,b)
    else:
        print('\033[91mError: The operation you select is not in our calculator.\033[0m')
while True:
    print()
    while True:
        try:
            number1=int(input('Enter 1st number : '))
            break
        except ValueError:
            print('\033[91mError: Only numbers are allowed.\033[0m')
    print()
    while True:
        try:
            number2=int(input('Enter 2nd number : '))
            break
        except ValueError:
            print('\033[91mError: Only numbers are allowed.\033[0m')
    print()
    print()
    print('''Select from the choices given below 
        1)Addition
        2)Subtraction
        3)Multiplication
        4)Division''')
    while True:
        try:
            operator=int(input('Enter the operation you want to perform : '))
            if 1<=operator<=4:
                break
            else:
                print('\033[91mError: Select 1 2 3 4 for desired operations.\033[0m')
        except ValueError:
            print('\033[91mError: Only numbers are allowed.\033[0m')
    print()
    print(calculator(number1,operator,number2))
    while True:
        ask=input('Want to continue (y/n) ?').lower()
        if ask=='y':
            break
        elif ask=='n':
            break
        else:
            print("\033[91mError: Select 'Y' or 'N'.\033[0m")
            continue
    if ask=='y':
        continue
    break