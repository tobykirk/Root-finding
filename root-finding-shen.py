def myfun(x):
    return x*x+(x-2)**3-5

def mybisection(a,b,epson):
    while abs(b-a) > epson:
        c0=(a+b)/2
        if myfun(c0)*myfun(b) < 0:
            a=c0
        else:
            b=c0
    print("a=,b=",a,b)

mybisection(0,10,0.01)
