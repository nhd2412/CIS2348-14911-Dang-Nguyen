# Dang Nguyen
# ID 1861688
# 5.19 CIS 2348 LAB*: Program: Automobile service invoice (Zylab)

print('Davy\'s auto shop services')
services = {'Oil change':35 , 'Tire rotation':19, 'Car wash':7 , 'Car wax':12}
print('Oil change -- ${}'.format(services['Oil change']))
print('Tire rotation -- ${}'.format(services['Tire rotation']))
print('Car wash -- ${}'.format(services['Car wash']))
print('Car wax -- ${}\n'.format(services['Car wax']))

first_service = input('Select first service:\n')
second_service = input('Select second service:\n\n')

print('Davy\'s auto shop invoice\n')
if first_service in services:
    print('Service 1: {}, ${}'.format(first_service,services[first_service]))
else:
    services[first_service] = 0
    print('Service 1: No service')
if second_service in services:
    print('Service 2: {}, ${}\n'.format(second_service,services[second_service]))
else:
    services[second_service] = 0
    print('Service 2: No service\n')
Total1 = services[first_service] + services[second_service]
print('Total: ${}'.format(Total1))