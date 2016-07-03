def get_even_list(fad):
    empty_list=[]
    for x in fad:
        if x%2==0:
            empty_list.append(x)
    return empty_list
get_even_list()

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
 print("Your function is correct")
else:
 print("Ooops, bugs detected")
