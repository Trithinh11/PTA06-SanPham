x = input().split(":")
hour = int(x[0])
minute = int(x[1])
second = int(x[2])

def kiemtra(h,m,s):
    if h > 23 or h < 0 or m > 0 or s > 59 or s < 0:
        return False
    else:
        return True
    
if kiemtra(hour, minute, second) == True:
    print("Hop le!")
else:
    print("khong hop le!")