#rabbits
def fib(n):                             #Dinh nghia ham fib(n)
    baby,mature = 0,1                   #thang0: so cap tho con = 0, tong so cap tho = 1
#Cong thuc tinh Pair tho thang thu n
    for i in range(n):                
        baby,mature=mature,baby+mature  #baby thang n=mature thang (n-1)
                                        #mature thang n = baby thang (n-1)+ mature thang (n-1)
    return total=mature+baby            #Ra cong thuc fib(n): total thang n = mature thang n + baby thang n
for i in range(5):                      #so thang chay tu 0 den 4
    print("Month ",i,": ",fib(i)," pair(s) of rabbits") #Hien thi ket qua: so pair tho lon thang thu i

    
