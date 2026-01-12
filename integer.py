
count2 = 0


for i in range(10,1000):
    if len(str(i)) == 2:
        if str(i)[0] > str(i)[1]:
            count2 += 1
            print(count2)
    elif len(str(i))  == 3:
        if str(i)[0] > str(i)[1] and str(i)[1] > str(i)[2]:
            count2 += 1
            print(count2)
    elif len(str(i))  == 4:
        if str(i)[0] > str(i)[1] and str(i)[1] > str(i)[2] and str(i)[2] > str(i)[3]:
             count2 += 1
             print(count2)