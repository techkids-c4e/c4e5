x=float(input('Nhap so thu nhat:'))
y=float(input('Nhap so thu hai:'))
i=str(input('Nhap dau'))
def calculator (x, i, y):
    if i == '+':
        answer = x + y
    elif i == '-':
        answer = x - y
    elif i == '*':
        answer = x * y
    elif i == '/':
        answer = x / y
    return answer
print(calculator(x, i, y)) 


    
