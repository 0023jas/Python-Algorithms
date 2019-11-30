integer = 1000000
while 1 == 1:
    integer += 1
    divisorList = []
    for i in range(integer):
        if i > 0:
            if (integer // i) == (integer / i):
                divisorList.append(1)

    if len(divisorList) <= 2:
        print(divisorList)
        print(integer)