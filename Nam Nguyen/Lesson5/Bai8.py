def get_even_list(l):
    k=[]
    for i in range(len(l)):
        if l[i] % 2 ==0:
            k.append(l[i])
    return k
el=get_even_list([1,2,5,-10,9,6])
if set(el)==set([2,-10,6]):
    print ('Your function is correct')
else:
    print('Ooops, bugs detected')

