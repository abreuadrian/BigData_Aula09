#Atividade 01
def get_nums():
    a = float(input('Informe um número: '))
    b = float(input('Informe outro número: '))
    return a, b

def summ(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def menu():
    dict_opt = {1: 'Soma',
                2: 'Subtração',
                3: 'Multiplicação',
                4: 'Divisão'}
    print()
    for x, y in dict_opt.items():
        print(f'[{x}] - {y} ')
    choice_menu(nums)

def choice_menu(nums):
    opt = int(input('\nSelecione sua opção: '))
    match opt:
        case 1:
            print(f'{summ(*nums):.2f}')
        case 2:
            print(f'{sub(*nums):.2f}')
        case 3:
            print(f'{mult(*nums):.2f}')
        case 4: 
            print(f'{div(*nums):.2f}')
        case _: 
            print('Selecione uma opção válida')


if __name__ == '__main__':
    nums = get_nums()
    menu()
