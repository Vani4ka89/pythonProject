# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return abs(self.area() - other.area())

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __len__(self):
        return self.x + self.y


rect1 = Rectangle(2, 4)
rect2 = Rectangle(3, 5)
print(rect1.area())
print(rect2.area())
print(rect1 + rect2)
print(rect1 - rect2)
print(rect1 == rect2)
print(rect1 != rect2)
print(rect1 < rect2)
print(rect1 > rect2)
print(len(rect1))
print(len(rect2))

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name

class Prince(Human):
    def __init__(self, name, age, boot_size):
        super().__init__(name, age)
        self.boot_size = boot_size

    def find(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.boot_size:
                return cinderella


class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        print(cls.__count)


cinderella1 = Cinderella('Cinderella1', 20, 35)
cinderella2 = Cinderella('Cinderella2', 22, 36)
cinderella3 = Cinderella('Cinderella3', 25, 37)
cinderella4 = Cinderella('Cinderella3', 24, 39)

prince = Prince('Prince', 30, 37)
found_cinderella = prince.find([cinderella1, cinderella2, cinderella3])

if found_cinderella:
    print('Cinderella found:', found_cinderella.name)
else:
    print('Cinderella not found:')

Cinderella.get_count()

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print() 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable 3) Створити клас Main в якому буде: - змінна класу printable_list яка буде зберігати книжки та журнали - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()

# для перевірки ксассів використовуємо метод isinstance, приклад:

# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")

class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)
        else:
            print("Помилка: можна додавати тільки книги та журнали")

    @classmethod
    def show_all_magazines(cls):
        print("Журнали:")
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        print("Книги:")
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()