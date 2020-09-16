#Dang Nguyen
#ID 1861688

#3.18 CIS 2348 LAB*: Program: Painting a wall (Zylab)

import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}


wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
paint_need = wall_area / 350
color = input()
print('Wall area: {} square feet'.format(wall_area))
print('Paint needed: {:.2f} gallons'.format(paint_need))
print('Cans needed: {} can(s)\n'.format(round(paint_need)))
print('Choose a color to paint the wall:')
print('Cost of purchasing {} paint: ${}'.format(color , paint_colors[color] * round(paint_need)))
