# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

from typing import Callable

def notebook()-> Callable[ str]:
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        return todo_list

    return add_todo, get_all

add_todo, get_all = notebook()

add_todo("Clean my room")
add_todo("Go to the shop")
add_todo("Play football")

print("All todos:")
for idx, todo in enumerate(get_all(), 1):
    print(f"{idx}. {todo}")

# 2) протипізувати перше завдання

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    number_str = str(num)
    expanded_form_list = []

    for i, digit in enumerate(number_str):
        if digit != '0':
            expanded_form_list.append(digit + '0' * (len(number_str) - i - 1))

    return ' + '.join(expanded_form_list)

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def decor(func):
    def box(*args, **kwargs):
        box.calls += 1
        print(f"Function '{func.__name__}' has been called {box.calls} times.")
        return func(*args, **kwargs)

    box.calls = 0
    return box

@decor
def func1(a, b):
    return a + b

@decor
def func2(a, b):
    return a * b

print(func1(22, 33))
print(func1(44, 55))
print(func2(2, 3))
print(func2(4, 5))


'''

1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
2) протипізувати перше завдання
"""
from typing import Callable


# def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add_nb1, get_all_nb1 = notebook()

add_nb1('ddddddd')
add_nb1('ffhhh')

print(get_all_nb1())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    # st = str(num)
    # length = len(st) - 1
    # res = []
    #
    # for i, ch in enumerate(st):
    #     if ch!='0':
    #         res.append(ch+'0'*(length-i))
    # return ' + '.join(res)
    return '+'.join(ch + '0' * (len(str(num)) - 1 - i) for i, ch in enumerate(str(num)) if ch != '0')


print(expanded_form(70304))


def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')

    return inner


@count_decor
def func1():
    print('func1')


@count_decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
func1()
func2()

'''