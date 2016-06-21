#rabbits
def fib(n):                             #Dinh nghia ham fib(n)
    baby,mature = 0,1                     #thang0: so cap tho con = 0, tong so cap tho = 1
#Cong thuc tinh Pair tho thang sau
    for i in range(n):                
        baby,mature=mature,baby+mature  #Pair tho con thang sau=pair tho lon thang truoc
                                        #pair tho lon thang sau = pair tho con thang truoc+ pair tho lon thang truoc
    return mature                       #Ra cong thuc fib(n)
for i in range(5):                      #Trong 4 thang dau tien
    print("Month ",i,": ",fib(i)," pair(s) of rabbits") #Hien thi ket qua: so pair tho lon thang thu i

    
