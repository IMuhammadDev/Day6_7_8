#  this program is about ' is number prime ?'

def prime_checker(number):
    count = 0
    for item in range(1, number + 1):
        if number % item == 0:
            count += 1
    if count == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
