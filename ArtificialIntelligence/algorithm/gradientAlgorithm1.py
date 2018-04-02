#encoding :utf-8

def PartialDerivative(x):
    x_new = 2*x-3
    return  x_new
def updateX(x,theTa):
    x = x - theTa*PartialDerivative(x)
    return x
def getY(x):
    y=(x*x-3*x+2)
    return  y
if __name__ =='__main__':
    x = 0
    y = getY(x)
    theTa = 0.5
    y_new =0
    while True:
        x = updateX(x,theTa)
        y_new = getY(x)
        if(abs(y_new - y)<0.00001):
            break
        y = y_new
    print x
    print y_new



