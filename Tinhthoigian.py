import datetime
import time
class Player:
    def __init__(self,ma,ten,timeIn,timeOut) :
        self.ma = ma
        self.ten = ten
        self.timeIn = timeIn
        self.timeOut = timeOut
        
    def timePlay(self):
        return (self.timeOut-self.timeIn).seconds
    
    def __lt__(self,other):
        return self.timePlay() > other.timePlay()
    
    def __str__(self):
        return f'{self.ma} {self.ten} {time.gmtime(self.timePlay()).tm_hour} gio {time.gmtime(self.timePlay()).tm_min} phut'
    

    
t = int(input())
players = []
while t>0:
    ma = str(input())
    ten = str(input())
    timeIn = datetime.datetime.strptime(str(input()),'%H:%M')
    timeOut = datetime.datetime.strptime(str(input()),'%H:%M')
    player = Player(ma, ten,timeIn,timeOut)
    players.append(player)
    t-=1
players.sort()

for player in players:
    print(player)
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Hai Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00