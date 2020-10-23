coordinates_1 = eval(input('Enter the first set of coordinates: '))
coordinates_2 = eval(input('Enter the second set of coordinates: '))

x_1, y_1 = coordinates_1
x_2, y_2 = coordinates_2

divisor = y_2 - y_1
dividend = x_2 - x_1

slope = divisor / dividend

original_equation = slope * x_1
y_int = y_1 - original_equation

if y_int >= 0:
    print(f'The equation of this line is y = {slope}x + {y_int}')

else:
    y_int -= y_int * 2
    print(f'The equation of this line is y = {slope}x - {y_int}')
