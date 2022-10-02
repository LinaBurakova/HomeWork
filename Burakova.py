import time
import requests
from lxml import html
import sqlite3


#так как распарсить сайт до конца не получилось, в базу данных были добавлены только 16 наименований
li1=[]
def name_box(xPath):
    url='https://griffonsocks.com.ua/product-category/dovgi/'
    response=requests.get(url)
    if response.status_code == 200:
        tree=html.fromstring(response.text)
        name=tree.xpath(xPath)
        li1.append(name)
        print(li1)

my_str='//*[@id="inner-content"]/div/ul/li[1]/h2/text()'
start = time.perf_counter()
li=[]


for i in range(1,17):
    new=my_str.replace('li[1]',f'li[{i}]')
    li.append(new)


# полученные данные запишем в документ, чтобы в дальнейшем парсер вывести в список из файла
for name in li:
    with open('text.txt', 'w') as file:
        name_box(name)
        file.write(str(li1))
with open('text.txt', 'r') as file:
    socks_list=file.readline()
    print(f'list: {socks_list}')


#корректируем список и обрезаем лишние символы с помощью преобразования в строку
a= ("".join(socks_list))
d=a.replace("[[",'')
f=d.replace(']]','')
h=f.replace("'","")
#затем режим с помощью split нашу строку в новый список
values1=h.split('], [')
print(f'Values: {values1}')
#создаем список из словарей, где один словарь представляет собой ключ-значение
#для всех ключекй keys = ['name'], а values = имя товара
keys = ['name']
zipped=zip(values1)
dicts = [dict(zip(keys, values)) for values in zipped]
print(dicts)

# создание таблицы на основании входящих данных
def create_socks():
    connect = sqlite3.connect('socks_data_base.db')
    cursor = connect.cursor()
    cursor.execute(
        'CREATE TABLE socks('
                   'name text, '    
                   ')'
    )
    connect.commit()

# добавление новых позиций в БД
def add_socks(socks: dict):
    connect = sqlite3.connect('socks_data_base.db')
    cursor = connect.cursor()
    print(list(socks.keys())[0])
    print(socks.values())
    request_in_socks = f'INSERT INTO socks' \
                       f' (name) ' \
                       f'VALUES ' \
                       f'("{socks["name"]}");'
    print(request_in_socks)
    cursor.execute(request_in_socks)
    connect.commit()

# вызов функции
for i in dicts:
    add_socks(i)




