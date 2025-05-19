
## 1
def bucle(num):
  for i in range(num):
    print(f'The for has been executed {i+1} times')

## 2
def suma (num1, num2, num3):
  result = num1 + num2 + num3
  return result

## 3
suma = lambda num1, num2, num3: num1 + num2 + num3

## 4
def comp_nombre(nombre):
  lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'
  for i in lista_nombre:
    if i == nombre:
      print(f'The name is in the list')


## 1/2 comprobación
sumed = suma(2,3,4)
print(sumed)

## 3 comprobación
bucle(2)
bucle(5)

## 4 comprobación
comp_nombre(nombre = 'Enrique')