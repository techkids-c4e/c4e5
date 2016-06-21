print('Exercise 3: To convert Celsius (°C) to Fahrenheit (°F)')
x = float(input('Celsius (°C): '))
y = x*1.8 + 32
print(str.format('Result: {0}°C = {1}°F',x,round(y,1)))
