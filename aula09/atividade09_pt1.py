#Atividade 01
def get_nums():
    n1 = float(input('Informe um número: '))
    n2 = float(input('Informe outro número: '))
    return n1, n2

def summ(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def menu(nums):
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
    menu(nums)
