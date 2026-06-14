def bisection(target, upper, lower):
    count = 20
    val = (upper + lower) / 2
    while(val != target and count > 0):
        if(val > target):
             upper = val
        else:
             lower = val
       
        val = (upper + lower) / 2
        count = count - 1
    return val;
   
print(bisection(3,10,1))