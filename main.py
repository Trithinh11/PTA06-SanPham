from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt6 import uic
import sys
import webbrowser

from model.account import Account

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
        self.btnSignUp.clicked.connect(self.ShowSignUp)
    def ShowSignUp(self):
        self.close()
        Su.show()

    def checkLogin(self):
        acc = Account()
        check = acc.checkAccount(self.txtUsername.text(), self.txtPassword.text())
        if check == True:
            self.close()
            Hp.show()
        else:
            htb = QMessageBox()
            #dat tieu de
            htb.setWindowTitle("Loi Dang Nhap")
            #dat Icon
            htb.setIcon(QMessageBox.Icon.Warning)
            #thong bao den nguoi dung
            htb.setText("Vui long kiem tra lai, tai khoan hoac mat khau da sai")
            #chinh style sheet
            htb.setStyleSheet("Background color: Yellow, color: black;")
            # sys.exit(htb.exec())
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui-GiaoDien/sign up.ui", self)
        # them su kien khi nhan vao nut dang ky
        self.btnsignup.clicked.connect(self.registerAccount)
        self.btnLogin.clicked.connect(self.ShowLogin)
    def ShowLogin(self):
        self.close()
        lg.show()

    def registerAccount(self):
        # doc thong tin nguoi dung nhap vao 
        username = self.txtEmail
        password = self.txtpassword
        comfirmPassWord = self.txtcomfirmpassword

        # dang nhap
        if username.text() == "":
            username.setFocus()
            return
        if password.text() == "":
            password.setFocus()
            return
        if comfirmPassWord.text() == "":
            comfirmPassWord.setFocus()
            return
        # neu nhu email khong dung dinh dang
        if username.text().find("@gmail.com") == -1:
            username.clear()
            username.setFocus()
            return
        # neu nhu mat khau sai va nhap lai mat khau thong dung
        if password.text() != comfirmPassWord.text():
            comfirmPassWord.setFocus()
            return
        # them tai khoan moi vao file
        with open("Data/Account.txt", "w") as file:
             file.write(username.text() + "," + password.text())
        lg.show()
        self.close()

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/homepage.ui", self)
        self.btnProfile.clicked.connect(self.showProfile)

        self.btnHome.clicked.connect(lambda: self.showpage(0))

        self.btnQTKH.clicked.connect(lambda: self.showpage(1))
        self.btnplayQTKH.clicked.connect(lambda: self.playMusic("C:\\Users\\ACER PHOENIX\\Downloads\\QTKH.mp4"))
        self.btnMrBeast.clicked.connect(lambda: self.showpage(2))
        self.btnplayMrBeast.clicked.connect(lambda: self.playMusic("C:\\Users\\ACER PHOENIX\\Downloads\\Mrbeast.mp4"))
        self.btnFreeFire.clicked.connect(lambda: self.showpage(3))
        self.btnplayFreeFire.clicked.connect(lambda: self.playMusic("C:\\Users\\ACER PHOENIX\\Downloads\\FreeFire.mp4"))
    def showProfile(sekf):
        Profile.show()

    def playMusic(self,link_music):
        webbrowser.open(link_music)
    def showpage(self,id):
        self.stackedWidget.setCurrentIndex(id)



class ProfilePage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/Profile.ui", self)
    
    def saveInfor(self):
        a = self.txtemail.text()
        b = self.txtphone.text()
        c = self.txtaddress.text()
        d = self.txtlovesong.text()
        e = self.txtloveartist.text()
        f = self.txtlovegenre.text()
        print(a,b,c,d,e,f,)

    def loadInfor(self):
        self.txtfullname.setText("Hong Quan beo")
        self.txtnickname.setText("Quan gayyyy")
        self.txtemail.setText("lehongquanbeo@gmail.com")
        self.txtphone.setText("0987654321")
        self.txtaddress.setText("948/16A duong lo gom")
        self.txtlovesong.setText("Thien Ly Oi")
        self.txtlovearetist("Jack")
        self.txtlovegenre("Rap")

        
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    lg = LoginPage()
    Su = SignUp()
    Hp = HomePage()
    Profile = ProfilePage()
    Su.show()
    app.exec()