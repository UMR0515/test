def rank(A1,A2,A3,A4,A5):
    if 500>=(A1+A2+A3+A4+A5)>=460:
        print("A")
    elif 459>=(A1+A2+A3+A4+A5)>=420:
        print("B")
    elif 419>=(A1+A2+A3+A4+A5)>=370:
        print("C")
    elif 369>=(A1+A2+A3+A4+A5)>=320:
        print("D")    
    else:
        print("E")
rank(70,80,90,95,85)
