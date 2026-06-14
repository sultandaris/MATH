def newton_raphson(a,n,p):
    count = p        
    x_lama = a/2
    while(abs(pow(x_lama,n)-a) > pow(10,-p)):
        turunan = n*pow(x_lama,n-1)
        x_baru = x_lama - ((pow(x_lama,n)-a)/turunan)
        print(x_baru)
        x_lama = x_baru
        count = count - 1
    print("\n")
    
    return x_lama
   
print(newton_raphson(2,3,5))