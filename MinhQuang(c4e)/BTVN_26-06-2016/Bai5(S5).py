def remove_dollar_sign(s):
    return s.replace('$','')
x = str(input('Please input clause: '))
print(remove_dollar_sign(x))
