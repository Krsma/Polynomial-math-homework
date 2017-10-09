

brojioci = [1, -1 ,2,-2,3,-3,4,-4,6,-6,12,-12]
imenilaci = [1, -1 ,2,-2,3,-3,5,-5,6,-6,10,-10,15,-15,30,-30]

def funkcija(a,b):
    n=a / b
    res=30*(n*n*n*n*n)-9*(n*n*n*n)-10*(n*n*n)+3*(n*n)-40*n+12
    if res==0:
        print(a)
        print(b)
        print()



for i in range(0,len(brojioci)):
    for j in range(0, len(imenilaci)):
        funkcija(brojioci[i],imenilaci[j])
