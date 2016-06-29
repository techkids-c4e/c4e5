#7
l=[1,4,5,-1,10]
def extract_even(l):
    
    new_list=[number for number in l if number%2==0]
    return new_list
print(extract_even(l))
get_even_list=extract_even

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")


