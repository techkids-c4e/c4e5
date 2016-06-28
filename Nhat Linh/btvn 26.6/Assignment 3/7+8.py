l=[1,4,5,-1,10]
def get_even_list(l):
    for x in l:
        if abs(x)%2==1:
            l.remove(x)
    return(l)


even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
 print("Your function is correct")
else:
 print("Ooops, bugs detected")
