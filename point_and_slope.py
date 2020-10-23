coordinates = eval(input('Enter the first set of coordinates: '))
slope = float(input('Enter the slope: '))

x_1, y_1 = coordinates

equation = slope * x_1
y_int = y_1 - equation

if y_int >= 0:
    print(f'The equation of this line is y = {slope}x + {y_int}')

else:
    y_int -= y_int * 2
    print(f'The equation of this line is y = {slope}x - {y_int}')
