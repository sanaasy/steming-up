# extra project
# greatest common divisor

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

def gcd (x, y):
    gcd = 1
    if x == 0 and y != 0:
        return gcd
    elif x != 0 and y == 0:
        return gcd
    else:
        if y > x:
            for i in range(int(y / 2), 0, -1):
                if x % i == 0 and y % i == 0:
                    gcd = i
                    break
            return gcd
        else:
            for i in range(int(x / 2), 0, -1):
                if x % i == 0 and y % i == 0:
                    gcd = i
                    break
            return gcd

print('The greatest common divisor is ', gcd(num1, num2))

# meg's way

gcd = 1
k = 2 # divisor

while k <= num1 and k <= num2:
    if num1 % k == 0 and num2 % k == 0:
        gcd = k
    k += 1
print('The greatest common divisor for', num1, 'and', num2, 'is', gcd)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial : "))
print(factorial(n))


x = int(input('enter: '))
d = 1
gcd2 = 1
list = []
while d <= x:
    if x % d == 0:
        gcd = d
        list.append(gcd)
    d += 1

print(list)

fruit1 = 'guava'
print(fruit1[:2])


