def level4(x):
    
    def sqrtIter(r):
        if f2(r):
            return r
        else:
            return sqrtIter(improve(r))
        
    def improve(r):
        return avg(r, x/r)
    
    def avg(x, y):
        return (x+y)/2
    
    def f2(r):
        if(abs(r**2-x)<0.001):
            return 1
        else:
            return 0
        
    return sqrtIter(1.0)
print(level4(int(input("Введите число: "))))    