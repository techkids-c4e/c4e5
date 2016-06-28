def even_list(l):
    k=[]
    for i in range(len(l)):
        if l[i] % 2 ==0:
            k.append(l[i])
    return k
x=input('Please input list of number: ')
x=eval(x)
print(even_list(x))
    
