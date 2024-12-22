#them thu vien can
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
#tao hop thong bao
htb = QMessageBox()
#dat tieu de
htb.setWindowTitle("Hop thong bao lop PtA06")
#dat Icon
htb.setIcon(QMessageBox.Icon.Warning)
#thong bao den nguoi dung
htb.setText("Ban co thuc su muon thoat khoi chuong trinh hay khong")
#chinh style sheet
htb.setStyleSheet("Background color: Yellow, color: black;")
sys.exit(htb.exec())