import math

## Ex. 1
list = ['Manzana', 'Pera']
tuple = ('Tarta de manzana', 'Pera al vino')
float = 5.44
int = 4
decimal = 5.44392021048
dict = {
    'Manzana':'Tarta de manzana',
    'Pera': 'Pera al vino'
    }

## Ex. 2
round_float = round(float, 1)
print(round_float)

## Ex. 3
sqrt_float = math.sqrt(float)
print(sqrt_float)

## Ex. 4
first_dict = dict['Manzana']
print(first_dict)

## Ex. 5
second_tuple = tuple[1]
print(second_tuple)

## Ex. 6
list.append('Limon')
print(list)

## Ex. 7
list[0] ='Uva'
print(list)

## Ex. 8
list.sort()
print(list)

## Ex. 9
tuple += ('Bizcocho de limon',)
print(tuple)