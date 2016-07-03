def remove_dollar_sign(Str):
    Str = Str.replace('$','')
    return Str

S = input('Enter your input String: ')
S = remove_dollar_sign(S)
print('String after removing all dollar sign $ :',S)
