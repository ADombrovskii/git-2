with open('D:\\Perepis.txt', 'r') as f:
    ot = int(input('от'))
    do = int(input('до'))

    for i in f:
        n = 0
        s = i.split()

        if int(s[3][len(s[3]) - 4 :]) < 1978:
            print(s[0])
            n += 1

        if (int(s[3][len(s[3]) - 4 :]) >= ot) and (int(s[3][len(s[3]) - 4 :]) <= do):
            print(s)