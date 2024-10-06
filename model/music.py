import webbrowser
class Music:
    def __init__(self, _l, _n, _a, _s, _d):
        self.link = _l
        self.name =  _n
        self.artist = _a
        self.stream = _s
        self.duration = _d
    #ham de mo bai hat
    def open(self):
        webbrowser.open(self.link)

# lay link tu youtube
ms1 = Music("https://www.youtube.com/watch?v=OrDB4jpA1g8", "JACK - J97 | THIÊN LÝ ƠI | Official Music Video", "Jack", 
"27.305.078 views", "5:08s")
ms1.open()
# lay link tu spotify
ms2 = Music("https://open.spotify.com/track/2AVDBKzxzTjLB91WVTfIlA?si=321ad46b0df84bc6", "Anh biết rồi", "Anh Trai Say Hi, Rhyder, Jmi Ko",
"2,522,599", "4:20s")
ms2.open()
