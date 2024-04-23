a = 12

a = 222
b = 33

if a == 22 and b != 33 or a < 100:
    print('boy')
else:
    print('girl')

print(a)

my_tuple = ('boy', 'girl')
print(my_tuple)
l = list(my_tuple)
print(tuple(l))

def count():
    res = [i for i in range(10, 100, 2)]
    return res

print(count())

def decor(func):

    def inner():
        print('*' * 20)
        func()
        print('*' * 20)

    return inner

@decor
def greeting():
    print('Hello from Python!')


print(greeting())

import time

def decor(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

@decor
def count():
    for i in range(100000000):
        pass

print(count())

name

def a():
    # name = 'Vasia'

    def b():
        # name = 'Petia'
        print(name)

    b()
    print(name)


a()
print(name)