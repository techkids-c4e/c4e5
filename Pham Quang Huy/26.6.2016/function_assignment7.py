def extract_even(list_):
    newlist = []
    for number in list_:
        if number % 2  == 0:
            newlist.append(number)
    return newlist
            
even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
