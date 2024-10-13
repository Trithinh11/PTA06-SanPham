
class Animal:
    #ham khoi tao
    def __init__(self, _n = "Chua biet", _a = 0):
        self.name = _n
        self.age = _a
    #ham in ra thong tin
    def show(self):
        print(self.__dict__)
    #ham tao tieng kieu dong vat
    def make_sound(self):
        print("Chua biet minh la dong vat gi, chua the keu duoc")
#tao ra thong tin lop con
class Dog(Animal):
    #da co init roi, khong con lam lai
    def __init__(self, _n="Chua biet", _a=0):
        super().__init__(_n, _a)
    #onerwirte make sound
    def make_sound(self):
        print("Gau Gau Gau")
        print("Canh nha Canh nha Canh nha")
#tao ra thong tin lop con
class Bird(Animal):
    #da co init roi, khong con lam lai
    def __init__(self, _n="Chua biet", _a=0):
        super().__init__(_n, _a)
    #onerwirte make sound
    def make_sound(self):
        print("chip chip chip")
        print("Bay Bay Bay")
#tao ra thong tin lop con
class Cat(Animal):
    #da co init roi, khong con lam lai
    def __init__(self, _n="Chua biet", _a=0):
        super().__init__(_n, _a)
    #onerwirte make sound
    def make_sound(self):
        print("Meo Meo Meo")
        print("Leo treo")
#tao ra thong tin lop con
class Reptile(Animal):
    #da co init roi, khong con lam lai
    def __init__(self, _n="Chua biet", _a=0):
        super().__init__(_n, _a)
    #onerwirte make sound
    def make_sound(self):
        print("fit fit fit")
        print("huc huc huc")
#tao ra thong tin lop con
class Fish(Animal):
    #da co init roi, khong con lam lai
    def __init__(self, _n="Chua biet", _a=0):
        super().__init__(_n, _a)
    #onerwirte make sound
    def make_sound(self):
        print("boc boc boc")
        print("boi boi boi")

list_animals = [
    Dog("Kiki", 3),
    Cat("Mimi", 2),
    Bird("Chim",3),
    Reptile("Bo sat", 2),
    Fish("Haha", 2)
]

print("Xin chao den voi so thu 3 anh em")
print("===========================")
print(f"Bay gio trong so thu hien dang co {len(list_animals)} loai dong vat")
print("==============================")
for animal in list_animals:
    print(f"xin chao, to ten la{animal.name}, day la tieng keu cua toi:")
    animal.make_sound()
print("===============================")