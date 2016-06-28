def remove_dollar_sign(Str):
    Str = Str.replace('$','')
    return Str

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print('Your function is correct')
else:
    print("Oops, there's a bug")
    
