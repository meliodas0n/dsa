def func1(number):
    print(f'func1 number : {number}')

def func2(number):
    print(f'func2 number : {number}')

def func3(number):
    print(f'func3 number : {number}')

number = int(input())
func_map = {1:func1, 2:func2}
func_map.get(number, func3)(number)
