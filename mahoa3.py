t = int(input())
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while t > 0:
    s =str(input())
    a = s[0:len(s)//2]
    b = s[len(s)//2:len(s)]
    tong = 0
    for i in a:
        tong += (ord(i) - ord('A'))
    sta=""
    for i in a:
        sta += (P[(ord(i) - ord('A') + tong) % 26])
    tong = 0
    stb = ""
    for i in b:
        tong += (ord(i) - ord('A'))
    for i in b:
        stb += (P[(ord(i) - ord('A') + tong) % 26])
    stt= ""
    for i in range(len(b)):
        stt += P[(ord(sta[i]) - ord('A') + ord(stb[i]) - ord('A') ) % 26  ]
    print(stt)
    t-=1