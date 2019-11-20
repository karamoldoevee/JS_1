foods = ['milk', 'beer', 'beer', 'milk', 'milk']

while True:
    for food in foods:
        if food == 'milk':
            print('Good')
        else:
            print('Bad')
    break



def mean(numbers):
    print(int((sum(numbers)) / max(len(numbers), 1)))
    return

mean([1, 5, 12, 4, 3])
mean([2, 3, 4, 5, 6, 7, 8, 9, 10])
mean([3, 10, 17])

def riddle():
    answer = input("У квадратного стола отпилили один угол. Сколько теперь углов у него стало? ")
    if answer == 5:
        print("Ответ верный")
    elif answer == 'пять':
        print("Ответ верный")
    elif answer == 'Пять':
        print("Ответ верный")
    else:
        print("Ответ неверный")
    return

riddle()

class Duck:
    def __init__(self, name, color, old):
        self.name = name
        self.color = color
        self.old = old

    def toStr(self):
        print(self.name, self.color, self.old)

    def say(self):
        print('Krya')

duck = Duck('Дональд', 'белый', 1)
duck.toStr()
duck.say()
