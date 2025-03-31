for A in range(500):
    flag = True
    for x in range(500):
        for y in range(500):
            if (((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 10))) == False:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
