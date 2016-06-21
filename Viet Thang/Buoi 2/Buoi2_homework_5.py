#Bai 5: Tinh so cap tho sau n thang

n = int(input("Ban can tinh so tho sau bao nhieu thang? "))

a0,a1 = 1,2 #gan so tho 2 thang dau

for time in range(n):
    if time == 0:
        print("Month",time,": Co",a0,"cap doi tho")
    elif time == 1:
        print("Month",time,": Co",a1,"cap doi tho")
    else:
        b = a1 #dung b lam so trung gian
        a1 = a0+ a1
        a0 = b
        print("Month",time,": Co",a1,"cap doi tho")
        

    
