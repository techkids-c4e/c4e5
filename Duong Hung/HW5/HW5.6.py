
def remove_dollar_sign(s):
    return s.replace('$','')

string_with_no_dollars = remove_dollar_sign("$80% perce$nt of l$ife is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print('Your finction is correct')
else:
    print('Oops. there is a big')
