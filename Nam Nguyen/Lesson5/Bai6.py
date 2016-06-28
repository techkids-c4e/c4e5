def remove_dollar_sign(str):
    print (str.replace("$",""))
    return str.replace("$","")
i= remove_dollar_sign("$80% percent of $life is showing $up")
if i == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

