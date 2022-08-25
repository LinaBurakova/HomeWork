print('Task 1')
# рассматривала объект с точки зрения продукта веб-страницы,
# для компании 'BMV', поэтому использовала критерии для изменения атрибутов именно
# для данного производителя
class Machine:
    def __init__(self,model, year, engine_volume, color, price):
        self.__model=model
        self.__year=year
        self.__producer='BMV'
        self.__engine_volume=engine_volume
        self.__color=color
        self.__price=price

    def getInfo(self):
        return f"Machine characteristics:\nmodel: {self.__model};\nyear: {self.__year};\nproducer: {self.__producer};\n" \
               f"engine_volume: {self.__engine_volume} l;\ncolor: {self.__color};\nprice: {self.__price} euro;"


    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_engine_volume(self):
        return self.__engine_volume

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        colors=['red','white','black','blue','gold','green']
        if new_color in colors:
            self.__color = new_color

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if str(new_price).isdigit() and int(price)>0:
            self.__price = new_price


model = input("Enter model: ")
models = ['1', '2', '3', '4', '5', '6', '7', '8', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', \
              'I3', 'I4', 'I8', 'IX', 'IX1', 'IX3']
while model not in models:
    print('Try again')
    model = input("Enter model: ")
year = int(input("Enter year: "))
while year<1929 or year>2022:
    print('Try again')
    year = int(input("Enter year: "))
engine_volume = float(input('Enter engine_volume: '))
while engine_volume<1.6 or engine_volume>5.6:
    print('Try again')
    engine_volume = float(input('Enter engine_volume: '))
color = input('Enter color: ')
price = int(input('Enter price: '))
car = Machine(model, year, engine_volume, color, price)
print()
print('Your result:\n',car.getInfo())
# #изменим цвет и цену для нашего объекта с помощью методов
car.set_color('blue')
car.set_price(80000)
print()
print('Changed result:\n',car.getInfo())

print()
print('Task 2')
#в классе "Книга" может измениться только свойство - "цена", поэтому все поля делаю с приватным доступом
#для 'Price' создаю сэттер с условиями, при которых можно изменить цену
#для остальных атрибутов сеттеры не создаю, так как не нужно менять их значения в классе
class Book:
    def __init__(self, name,year,publishing, genre,author,price):
        self.__name=name
        self.__year1=year
        self.__publishing=publishing
        self.__genre=genre
        self.__author=author
        self.__price1=price


    def get_MyBook(self):
        return f'Name: {self.__name};\nYear: {self.__year1};\nPublishing: {self.__publishing};\nGenre:{self.__genre};' \
               f'\nAuthor: {self.__author};\nPrice: {self.__price1} hrn'

    def get_name(self):
        return self.__name

    def get_year1(self):
        return self.__year1

    def get_publishing(self):
        return self.__publishing

    def get_genre(self):
        return self.__genre

    def get_genre(self):
        return self.__genre

    def get_price1(self):
        return self.__price1

    def set_price(self, price):
        if str(price).isdigit() and int(price)>0:
            self.__price1 = price

myBook = Book('Saturday', 2005, 'Ranok', 'thriller', 'Ian Russell McEwan',100)
print(myBook.get_MyBook())
myBook.set_price(150)
print()
print(myBook.get_MyBook())
print()
print('Task 3')
#в существующем стадионе мы можем поменять имя (пример: в г.Днепр был стадион "Трудовые резервы" стал
# "Олимпийские резервы". И вместимость стадиона тоже может изменяться после реконструкции.
# Поэтому сеттеры добавлены к атрибутам nameStadion и capacity
class Stadion:
    def __init__(self, nameStadion,date,country,city,capacity ):
        self.__nameStadion=nameStadion
        self.__date=date
        self.__country=country
        self.__city=city
        self.__capacity=capacity


    def get_StadionInfo(self):
        return f'Name: {self.__nameStadion};\nDate: {self.__date};\nCountry: {self.__country};\nCity:{self.__city};' \
               f'\nCapacity: {self.__capacity} place;'

    def get_nameStad(self):
        return self.__nameStadion

    def set__nameStad(self, name):
        self.__nameStadion=name

    def get_date(self):
        return self.__date

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_capacity(self):
        return self.__capacity

    def set__capacity(self, capacity):
        if str(capacity).isdigit() and int(capacity)>0:
            self.__capacity=capacity

StadionDinamo=Stadion('Dinamo','12 June 1933','Ukraine', 'Kiev','16873')
print(StadionDinamo.get_StadionInfo())
StadionDinamo.set__nameStad('Peremoga')
StadionDinamo.set__capacity(20000)
print()
print(StadionDinamo.get_StadionInfo())