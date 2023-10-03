def ATriangle(b, h):
    return b*h/2

def TTriangle(a, b, c):
    return (a<b+c and b<a+c and c<a+b)

def TTriangle90(a, b, c):
    if(not TTriangle(a,b,c)):
        print("Error 001: No triangle")
        return None
    elif(a>=b and a>=c):
        return (a*a==b*b+c*c)
    
    elif(b>=a and b>=c):
        return (b*b==a*a+c*c)
    
    elif(c>=b and c>=a):
        return (c*c==a*a+b*b)

def ASquare(b, h):
    return b*h

def VCube(b, h, p):
    return b*h*p

def Fibonacci(n):
    if n<0:
        return None
    elif n==0:
        return 0
    elif n<3:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
def Factorial(n):
    if n>996:
        print("Error 002: recursion limit exceeded")
        return None

    elif n<0:
        return None
    
    elif n==0:
        return 1
    
    else:
        return n*Factorial(n-1)