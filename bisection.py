def bisection(a,n,p):
    upper = a
    lower = 0
    val =  pow((upper+lower)/2,n) - a
    while(abs(((upper+lower)/2)-lower) > pow(10,-p)):
        if(val > 0):
             upper = (upper+lower)/2
        else:
             lower = (upper+lower)/2
        print(((upper+lower)/2)-lower)
        val =  pow((upper+lower)/2,n) - a
    print("end\n")
    
    return (upper+lower)/2

print(bisection(2,3,5))
