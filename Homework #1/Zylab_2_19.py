# Dang Nguyen
# ID 1861688
# 2.19 CIS 2348 LAB*: Program: Cooking measurement converter (Zylab)

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
amount_serving = float(input('How many servings does this make?\n\n'))

print('Lemonade ingredients - yields','{:.2f}'.format(amount_serving), 'servings')
print('{:.2f}'.format(lemon_juice_cups),'cup(s) lemon juice')
print('{:.2f}'.format(water_cups) ,'cup(s) water')
print('{:.2f}'.format(agave_nectar_cups) ,'cup(s) agave nectar\n')

amount_serving2 = float(input('How many servings would you like to make?\n\n'))
print('Lemonade ingredients - yields','{:.2f}'.format(amount_serving2), 'servings')
print('{:.2f}'.format((amount_serving2/amount_serving)*lemon_juice_cups),'cup(s) lemon juice')
print('{:.2f}'.format((amount_serving2/amount_serving)*water_cups),'cup(s) water')
print('{:.2f}'.format((amount_serving2/amount_serving)*agave_nectar_cups),'cup(s) agave nectar\n')

print('Lemonade ingredients - yields','{:.2f}'.format(amount_serving2), 'servings')
print('{:.2f}'.format(((amount_serving2/amount_serving)*lemon_juice_cups)/16),'gallon(s) lemon juice')
print('{:.2f}'.format(((amount_serving2/amount_serving)*water_cups)/16),'gallon(s) water')
print('{:.2f}'.format(((amount_serving2/amount_serving)*agave_nectar_cups)/16),'gallon(s) agave nectar')

# FIXME (1): Finish reading other items into variables, then output the three ingredients
   
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# FIXME (3): Convert and output the ingredients from (2) to gallons
   
