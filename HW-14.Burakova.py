print('Task 1')
#в классе "Книга" может измениться только свойство - "цена", поэтому все поля делаю с приватным доступом
#для 'Price' создаю сэттер с условиями, при которых можно изменить цену
#для остальных атрибутов сеттеры не создаю, так как не нужно менять их значения в классе
class Book:
    def __init__(self, name,year,publishing, genre,author,price):
        self.__name=name
        self.__year=year
        self.__publishing=publishing
        self.__genre=genre
        self.__author=author
        self.__price = 0

        self.set_price(price)

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_publishing(self):
        return self.__publishing

    def get_genre(self):
        return self.__genre

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if str(price).isdigit() and int(price) > 0:
            self.__price = price

    def get_MyBook(self):
        return {'name':self.__name, 'year':self.__year,'publishing':self.__publishing, 'genre':self.__genre,\
                'author': self.__author, 'price': self.__price}

    def __str__(self):
        return f'Name: {self.__name};\nYear: {self.__year};\nPublishing: {self.__publishing};\nGenre: {self.__genre};' \
               f'\nAuthor: {self.__author};\nPrice: {self.__price} hrn'

#унаследуем все атрибуты базового класса Book и добавим новые свойства pages и website,
# где свойство "website" может изменяться в зависимости есть ли у журнала электронная версия
class Magazine(Book):
    def __init__(self, name,year,publishing, genre,author,price, pages, website):
        super().__init__(name,year,publishing, genre,author,price)
        self.__pages=pages
        self.__website = 0

        self.set_website(website)


    def __str__ (self):
        return f'{super().__str__()}\nPages: {self.__pages} pages; \nOnline: {self.__website};'

    def get_pages(self):
        return self.__pages

    def get_website(self):
        return self.__website

    def set_website(self, website):
        if website=='Yes' or website=='No':
            self.__website = website


magazine1=Magazine('National Geographic ','June 2022','NG Media','science','Nathan Lump',150,35,'Yes')
print(magazine1)
print( '\nChanged info:')
magazine1.set_price(220)
magazine1.set_website("No")
print(magazine1)

print()
print('Task 2')
#используем множественное наследованиеююMagazine будет родителем для Newspaper, в котором добавим
# новые атрибуты country, circulation
class Newspaper(Magazine):
    def __init__(self,name,year,publishing, genre,author,price, pages, website, country, circulation):
        super().__init__(name,year,publishing, genre,author,price, pages, website)
        self.__country=country
        self.__circulation=circulation

    def __str__ (self):
        return f'{super().__str__()}\nCountry: {self.__country}; \nCirculation: {self.__circulation} print;'

    def get_country(self):
        return self.__pages

    def get_circulation(self):
        return self.__circulation

    def set_circulation(self, circulation):
        if str(circulation).isdigit() and int(circulation) > 0:
            self.__circulation = circulation

newspaper1=Newspaper('The New York Times','15th of May 2022','Times Books','news','Joseph Kahn',65, 22,'Yes','USA', 780000)
print(newspaper1)
print( '\nChanged info:')
newspaper1.set_price(99)
newspaper1.set_circulation(650000)
newspaper1.set_website("No")
print(newspaper1)