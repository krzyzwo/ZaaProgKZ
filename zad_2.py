class Library:
    def __init__(self, city, street, zip_code, open_hours:str, phone):
        self.city  = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f'{self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone}'
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone}'
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f'{self.library}, {self.publication_date}, {self.author_name}, {self.author_surname}, {self.number_of_pages}'
class Order:
    def __init__(self, employee, student, books:list[Book], order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        ksiazki: str = ""
        for book in self.books:
            ksiazki = (ksiazki + " " + str(book) + ",")
        return f'{self.employee}, {self.student}, {ksiazki} {self.order_date}'
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f'{self.name}'



Katowicka = Library('Katowice', 'Armii Krajowej', '40-002', '8-20', '222000444')
Tyska = Library('Tychy', 'Policyjna', '42-034', '10-21', '022194676')
Hobbit = Book(Katowicka, 1999, 'J.R.R.', 'Tolkien', 232)
Godfather = Book(Tyska, 1967, 'Mario', 'Puzo', 630)
Zarathustra = Book(Katowicka, 1887, 'Fryderyk', 'Nietche', 262)
Sztuka_Wojny = Book(Katowicka, -600, 'Sun', 'Tsu', 192)
Uczta = Book(Tyska, -600, 'Platon', '', 280)
AnnaJ = Employee('Anna', 'Jeleń', '5.02.2026', '23.10.2000', 'Katowice', 'Armi Krajowej', '40-235', 221587296)
KorneliuszG = Employee('Korneliusz', 'Gołąb', '1.07.2025', '6.02.2004', 'Tychy', 'Cicha', '42-382', 206984379)
MaciejP = Employee('Maciej', 'Pawłowicz', '28.06.2018', '2.11.1999', 'Katowice', 'Hallera', '40-247', 849267672)
Szymon = Student('Szymon', 80)
Przemek = Student('Przemysław', 70)
Marcin = Student('Marcin', 36)
Zamowienie1 = Order(KorneliuszG, Przemek, [Hobbit, Uczta], '2.11.2026')
Zamowienie2 = Order(AnnaJ, Szymon,[Sztuka_Wojny, Godfather], '22.10.2026')

print(Zamowienie1)
print("")
print(Zamowienie2)

