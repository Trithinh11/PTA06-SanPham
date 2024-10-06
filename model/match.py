import webbrowser
class Football:
    def __init__(self, _l, _n, _m, _v, _r, _t1, _t2):
        self.link = _l
        self.name = _n
        self.match = _m
        self.views = _v
        self.result = _r
        self.team1 = _t1
        self.team2 = _t2
    
    def open(self):
        webbrowser.open(self.link)
    def openlink1(self):
        webbrowser.open(self.team1)
    def openlink2(self):
        webbrowser.open(self.team2)

fb1 = Football("https://www.youtube.com/watch?v=UWK7da4T9SM", "HIGHLIGHTS: MAN UNITED - MAN CITY | ĐẤU SÚNG SIÊU CĂNG THẲNG, BERNARDO SILVA TẠO BƯỚC NGOẶT", "MU vs MC", 
"1.078.200 views", "Manchester City win 1-1, penalty 7-6", "https://www.manutd.com/", "https://www.mancity.com/")

fb2 = Football("https://www.youtube.com/watch?v=8-UsY1gOOsE", "ARSENAL - CHELSEA | EMIRATES RỰC LỬA, CƠN MƯA BÀN THẮNG TẠI DERBY LONDON | NGOẠI HẠNG ANH 23/24", 
"Arsenal vs Chelsea", "2.298.561", "Arsenal win 5-0", "https://www.arsenal.com/", "https://www.chelseafc.com/en")
