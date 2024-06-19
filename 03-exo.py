a = float(input('Enter a first value : '))
b = float(input('Enter a second value : '))
c = float(input('Enter a third value : '))

if a + b > c and a + c > b and b + c > a:
  print (f"these values {a}, {b} and {c} can make triangle")
else:
  print(f' these values {a}, {b} and {c} can"t make triangle ')