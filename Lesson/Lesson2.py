class cho:
    def __init__(self, n = "chua biet", s = "chua biet", o = "chua biet", c = "chua biet", w = "chua biet"):
        self.name = n
        self.species = s
        self.old = o
        self.color = c
        self.weight = w
    
    def show(self):
        print(self.__dict__)
    
    cho = cho()
    cho.show()
    




exit()
class Xe:
    def __init__(self, _hx = "Chua biet", _scn = "Chua biet", _sms = "Chua biet"):
        self.hangxe = _hx
        self.sochongoi = _scn
        self.mausac = _sms
    #ham de show thong tin cua lop
    def show(self):
        #ham duoc dung san de in ra tat ca thuoc tinh co trong class
        print(self.__dict__)

class XeDap(Xe):
    def __init__

# Truong hop chua truyen tham so vao
xe1 = Xe()
xe1.show()
#Truong hop
xe2 = Xe("Vinfast")
xe2.show()

xe3 = Xe("Vinfast", 2)
xe3.show()

xe4 = Xe("Vinfast", 2, "Trang")
xe4.show()