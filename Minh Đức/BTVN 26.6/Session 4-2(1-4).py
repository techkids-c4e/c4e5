ship_list = [5,7,300,90,24,50,75]
#2.1
print('Hello, my name is Duc and here is my flock')
print(ship_list)
def nhieu_bai_qua():
    #2.2
    print('Now my biggest sheep has size',max(ship_list),'lets shear it')
    #2.3
    print('After shearing, here is my flock')
    ship_list[ship_list.index(max(ship_list))]=8
    print(ship_list)
nhieu_bai_qua()
empty_list=[]
def hu_hu():
    #2.4
    print('One month has passed, now here is my flock')
    for i in ship_list:
        empty_list.append(i+50)
hu_hu()
print(empty_list)
    
