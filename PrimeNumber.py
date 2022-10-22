number = int(input('enter any number:'))
for i in range(2, number):
    if number % i == 0:
        print('Not a prime number!')
        break

else:
    print("It's prime number!")