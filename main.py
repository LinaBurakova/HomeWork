import json

#для serialize наших объектов класса был добавлен метод (def __dict__),
# который преобразовывает атрибуты класса в поля словаря
# Вызов метода __dict__ и запись данных в файл происходит на строках 134-141
class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()
    __indicator = None

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def set_indicator(self, indicator: str):
        self.__indicator=indicator

    def get_indicator(self):
        return self.__indicator

    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(f'{self.__indicator} {self.__str__() }\n')

    def __dict__(self):
        return {'firstname': self.__firstname,
                'lastname': self.__lastname,
                'phone': self.__phone}


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)
        super().set_indicator('student')

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        return f'{super().__str__()} {self.__group}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_group(res[3])

    def __dict__(self):
        dict_st={"group":self.__group}
        dict_per= super().__dict__()
        dict_per.update(dict_st)
        return dict_per


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)
        super().set_indicator('teacher')

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_subject(res[3])

    def __dict__(self):
        dict_teach={"group":self.__subject}
        dict_per= super().__dict__()
        dict_per.update(dict_teach)
        return dict_per

li = []
li.append(Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'))
li.append(Teacher('Nikolay','Ivashenko','09878909990','JavaScript'))
li.append(Teacher('Alexsandr','Vetrov','087897789888','SMM'))
li.append(Teacher('Georg','Mamaev','678766778877','HTML'))
li.append(Teacher('Lubov','Nikolaeva','876789876889','CSS'))

#создаем список, в который будет добавлен словарь и отправлен в файл на запись
li_general=[]

for i in li:
    li_general.append(i.__dict__())
    with open('serialize.txt', 'w') as file:
        json.dump(li_general,file,indent=2)

with open("serialize.txt") as file:
    json_data = json.load(file)
    print(json_data)


class Group:
    __name = str()
    __li = list()

def __init__(self, name: str):
    self.set_name(name)

def set_name(self, name: str):
    self.__name = name

def get_name(self):
    return self.__name

def append(self, person: Person):
    self.__li.append(person)

def li_from_file(filename: str = 'text.txt'):
    with open(filename, 'r') as file:
        li=[]
        persons = file.readlines()
        for person in persons:
            person = person.split()
            if person[0] == 'student':
                li.append(Student(person[1], person[2], person[3], person[4]))
            if person[0] == 'teacher':
                li.append(Teacher(person[1], person[2], person[3], person[4]))
    return li

