def myfun(x):
    return x**2+(x-2)**3-5

def myfun2(x):
    return x**3+(x-2)**3-5


def mybisection(f,a,b,eps):

    #initial guess
    x=(a+b)/2.0
    err=b-a
    
    if f(a)*f(b) > 0:
        raise ValueError("Possible no root in given interval")

    while err > eps:
        if f(a)*f(x) < 0:
            b=x
        else:
            a=x
        err=b-a
        x=(a+b)/2
    return x        



x = mybisection(myfun,-3.,3.,10**(-6))
print(x)
    
