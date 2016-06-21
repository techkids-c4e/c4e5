initial_number=int(input("Initial B bacteria number : ")) #Nhap so luong vi khuan ban dau
time=float(input("Period of time : ")) #Nhap so phut
total_B=int(initial_number*(2**(time//2))) #tinh tong so vi khuan
print("After ",time," minutes we would have",total_B," bacteria(s)") #Hien thi ket qua
