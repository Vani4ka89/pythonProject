# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

def notebook():
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