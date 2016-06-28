#Option 1
def extract_even_1(l):
    return[i for i in l if i % 2 == 0] #to remove i if i%2==0

#Option 2
def extract_even_2(l):
    for i in l:
        if i % 2 == 1:
            l.remove(i) #to remove i
    return l

#Option 3
def extract_even_3(l):
    a=[]
    for i in l:
        if i%2 == 0:
            a.append(i) #to add i into list a
    return a

even_list = extract_even_1([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Correct")
else:
    print("Bug detected")

even_list = extract_even_2([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Correct")
else:
    print("Bug detected")

even_list = extract_even_3([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Correct")
else:
    print("Bug detected")       
