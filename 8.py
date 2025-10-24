def gcd_recursive(a,b):
    if(b==0):
        return abs(a)
    else:
        print("gcd_recursive({},{})".format(a,b))
        return gcd_recursive(b,a%b)

gcd_recursive(35,14)

def default_parameter(a,b=12):
    print(a+b)

default_parameter(2)
default_parameter(2,5)