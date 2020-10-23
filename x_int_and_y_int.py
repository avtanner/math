x_int_value = int(input('Enter the x-intercept: '))
y_int_value = int(input('Enter the y_intercept: '))

slope = y_int_value / x_int_value

if y_int_value >= 0:
    print(f'The equation of this line is y = {slope}x + {y_int_value}')

else:
    y_int_value -= y_int_value * 2
    print(f'The equation of this line is y = {slope}x - {y_int_value}')
