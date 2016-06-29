#LIST OF STRING

##in list mau
colors_list=['Blue','Red','Black','Pink','Brown','Yellow']
print('My color list : ',colors_list)

##in mau vi tri 3
print('colors_list at index 3: ',colors_list[3])

##in mau o vi tri do ng dung nhap
i=int(input('enter a number from 0-5: '))
print('your color: ',colors_list[i])

##in list 2 cach
print(colors_list)
# va
for color in colors_list:
    print(color)

##hoi mau yeu thich, co trong list thi tim index, k co thi bao k co
i=input('what is your favourite color? ')
if i in colors_list:
    print('your color is at index ',colors_list.index(i),' in my list')
else:
    print('sorry, i could not find your color')


