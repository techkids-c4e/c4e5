#5-6
def remove_dollar_sign(s):
    remove_dollar_sign=s.replace('$','')
    return remove_dollar_sign

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
print(string_with_no_dollars)
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

    

