# FizzBuzz

def fizzbuzz(contmax):
  cont = 1
  while cont <=contmax:
    if cont%3 == 0 and cont%5 == 0:
      print('FIZZ BUZZ')
    if cont%3 == 0 and cont%5 != 0:
      print('FIZZ')
    if cont%3 != 0 and cont%5 == 0:
      print('BUZZ')
    if cont%3 != 0 and cont%5 != 0:
      print(cont)
    cont +=1
    

fizzbuzz(10)