ship_list = [5,7,300,90,24,50,75]
print('Hello, my name is Duc and here is my flock')
print(ship_list)
def nhieu_bai_qua():
    print('Now my biggest sheep has size',max(ship_list),'lets shear it')
    print('After shearing, here is my flock')
    ship_list[ship_list.index(max(ship_list))]=8
    print(ship_list)
def hu_hu():
    print('One month has passed, now here is my flock')
    ship_list[:] = [x + 50 for x in ship_list]
    print(ship_list)
x=int(input('Please enter month: '))
for thang in range(1,x+1):
    print('MONTH', thang)
    hu_hu()
    nhieu_bai_qua()
tong=ship_list[0]+ship_list[1]+ship_list[2]+ship_list[3]+ship_list[4]+ship_list[5]+ship_list[6]
print('My flock has size in total: ',tong)
print('I would get',tong,' * 2$ = ',tong*2,'$')
