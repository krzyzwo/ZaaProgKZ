class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

Przemek = Student("Przemysław", 70)
Marcin = Student("Marcin", 36)

def ispassed(self) -> bool:
    if self.marks > 50:
        print(f'{self.name} jest {True}')
        return True
    else:
        print(f'{self.name} jest {False}')
        return False

ispassed(Przemek)
ispassed(Marcin)