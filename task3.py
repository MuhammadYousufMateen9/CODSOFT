import random
alphabets='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha=random.choice(alphabets)
digits='0123456789'
num=random.choice(digits)
special_characters='@.!#$%^&*()_+|}{"<?/,\';\\][=-]}'
sc=random.choice(special_characters)
characters=digits+alphabets+special_characters
alphanumeric=digits+alphabets
password=''
while True:
    try:
        length_ask=int(input('Enter the length of password : '))
        if length_ask>=8:
            break
        else:
            print('\033[91mError: Password length must be atleast 8.\033[0m')
    except ValueError:
        print('\033[91mError: Answer must be an integer.\033[0m')
print('''Select the type of complexity
      1)Strong Password: It will contain letters, numbers and symbols.
      2)Fair Password: It will contain letters and numbers only.
      3)Weak Password: It will contain letters only.
      4)Poor Password: It will contain digits only. ''')
while True:
    try:
        complexity_ask=int(input('Choose the complexity of your password : '))
        if complexity_ask==1:
            for i in range(length_ask-3):
                password+=random.choice(characters)
            password+=num+alpha+sc
            break
        elif complexity_ask==2:
            for i in range(length_ask-3):
                password+=random.choice(alphanumeric)
            password+=num+alpha
            break
        elif complexity_ask==3:
            for i in range(length_ask):
                password+=random.choice(alphabets)
            break
        elif complexity_ask==4:
            for i in range(length_ask):
                password+=random.choice(digits)
            break
        else:
            print('\033[91mError: Select 1 2 3 4 for the desired option.\033[0m')
            continue
    except ValueError:
        print('\033[91mError: Answer must be an integer.\033[0m')
print(f'Your password is : {password}')
