#Bai 4: Tinh so vi khuan B sau thoi gian nhat dinh
B = int(input("Hien dang co bao nhieu vi khuan B? "))
Time = int(input("Can tinh so vi khuan sau bao nhieu phut? "))
Sovikhuan = B*(2**(Time//2))
print("Sau",Time,"phut se co",Sovikhuan,"vi khuan B")
