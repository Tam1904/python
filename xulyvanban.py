while True:
    try:
        s = str(input()).strip()
        s = s.lower()
        tmp = ''
        s = s.replace('.','///').replace('?','///').replace('!','///')
        for x in s.split('///'):
            for y in x.split():
                if tmp == '':
                    tmp+=y.title() + ' '
                else :
                    tmp+=y + ' '
            print(tmp.strip())
            tmp = ''
    except EOFError:
        break
# ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam! vay CO PHAI NAM NAY LA KY THI LAN THU 10?
# khong phai! nam nay la KY THI LAN THU 11.