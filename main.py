import math

print('📚📏📐 Calculate area of a triangle')
print('''\nOptions:
1. Calculate area with base and height
2. Calculate area with two sides and an angle
3. Calculate area with 3 sides
4. Calculate area of a Equilateral triangle with a side
5. Calculate area of a Isosceles
''')

op_num = input('Enter the number of your choosen option: ')
print('\n')

if '1' in op_num:
    a = float(input('Enter the value of the base: '))
    b = float(input('Enter the value of the height: '))
    area = 0.5 * a * b
    print(f'The area of the triangle is {area} unit²')

elif '2' in op_num:
    a = float(input('Enter the value of the first side: '))
    b = float(input('Enter the value of the second side: '))
    θ = float(input('Enter the value of the angle(°): '))
    sinθ = math.sin(math.radians(θ))
    area = 0.5 * a * b * sinθ
    print(f'The area of the triangle is {area} unit²')

elif '3' in op_num:
    a = float(input('Enter the value of the first side: '))
    b = float(input('Enter the value of the second side: '))
    c = float(input('Enter the value of the third side: '))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = round(area, 4)
    print(f'The area of the triangle is {area} unit²')

elif '4' in op_num:
    a = float(input('Enter the value of the side: '))
    area = (math.sqrt(3) * (a * a)) / 4
    area = round(area, 4)
    print(f'The area of the trangle is {area} unit²')

elif '5' in op_num:
    a = float(input('Enter the value of the equal side: '))
    b = float(input('Enter the value of the base: '))
    area = (b * math.sqrt((4 * (a * a)) - (b * b))) / 4
    area = round(area, 4)
    print(f'The area of the triangle is {area} unit²')

else:
    print('You entered wrong!')
