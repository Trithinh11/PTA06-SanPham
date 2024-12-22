class Account:
    def __init__(self, _un = "Tai Khoan", _pw = "123"):
        self.username = _un
        self.password = _pw
        self.loadDataFromFile()
    #ham in ra thong tin tai khoa
    def show(self):
         print(self.__dict__)
        #ham luu thong tin tu file
    def saveDataToFile(self):
        #mo file duoi dang viet
        with open("Data/Account.txt", "w") as file:
            data = ""
            data += self.username +","
            data += self.password 
            #ghi file vao
            file.write(data)
    #ham doc thong tin tu file
    def loadDataFromFile(self):
        #mo file duoi dang hoc
        with open("Data/Account.txt", "r") as file:
            #doc het tat ca cac dong
            data = str(file.readline())
            #chia du lieu thanh tung thuoc tinh
            self.username, self.password  = data.split(",")
    #ham doi mat khau
    def changePassword(self,newPassword):
        self.password = newPassword 
        self.saveDataToFile()
    #ham kiem tra dang nhap
    def checkAccount(self,_un, _pw):
        if _un == self.username and _pw == self.password:
            return True
        else:
            return False 




