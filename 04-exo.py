user_number = int(input('Please enter a number: '))
# check if the number is Prime number

if user_number > 1:
    for i in range(2, user_number):
        if (user_number % i) == 0:
            print(f'{user_number} is not a prime number')
            break
        else:
          print(f'{user_number} is a prime number')