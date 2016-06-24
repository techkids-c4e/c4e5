## tinh tong so doi tho sau 5 tháng

t0=1 #so doi tho thang dau
t1=2 #so doi tho thang 2

for i in range(15):
    if (i<2):
        print(str.format('Thang {0} co {1} doi tho',i,i+1))
    if (i>1):
        x=t1
        t1=t0+t1
        t0=x
        print(str.format('Thang {0} co {1} doi tho',i,t1))
