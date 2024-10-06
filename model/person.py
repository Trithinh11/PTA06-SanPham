exit()
class Person:
    def __init__(self, _cP, _aP, fn, nn, bt, rl, ed):
        #ham khoi tao-> khi minh tao ra mot doi tuong moi
        self.coverpicture = _cP
        self.avatarPicture = _aP
        self.fullname = fn
        self.nickname = nn
        self.birthday = bt
        self.relationship = rl
        self.education = ed
    #ham de ghi ra thong tin cua nguoi do
    def show(self):
         print(self.__dict__)
    #ham luu thong tin vao file
    def saveDataToFile(self):
        #mo file duoi dang viet
        with open("person.txt", "w") as file:
            data = ""
            data += self.coverpicture +","
            data += self.avatarPicture +","
            data += self.fullname +","
            data += self.nickname +","
            data += self.birthday +","
            data += self.relationship +","
            data += self.education +""
            #ghi file vao
            file.write(data)
    #ham doc thong tin tu file
    def loadDataFromFile(self):
        #mo file duoi dang hoc
        with open("person.txt", "r") as file:
            #doc het tat ca cac dong
            data = (file.readline())
            #chia du lieu thanh tung thuoc tinh
            self.coverpicture, self.avatarPicture, self.fullname, self.nickname, self.birthday, self.relationship, self.education = data.split(",")
            

ps1 = Person("", "", "", "", "", "", "")
ps1.loadDataFromFile()
ps1.show()