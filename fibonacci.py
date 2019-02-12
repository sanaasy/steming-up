# Sanaa Syed
# 20/07/2018
# Selection structures homework

# loop statement problem - fibonacci sequence
# 1. ask the user how many numbers from the Fibonacci sequence they want to generate
n = int(input('How many numbers from the Fibonacci sequence do you want to generate? '))
def fib_sequence(n): # create a function for the while loop
    i = 0
    num = 1
    previous_num = 0
    while (i < n) :
            nextterm = num + previous_num
            num = previous_num
            previous_num = nextterm
            i = i + 1
            print(nextterm)
fib_sequence(n)
print('')

# fibonacci sequence using a for loop
def fibonacci(n):
    first = 0
    second = 1
    print(second)
    for i in range(0, n - 1):
        third = first + second
        first = second
        second = third
        print(third)
fibonacci(n)
print('')

# another way to solve this
n1 = 0
n2 = 1
count = 1

if n <= 0 :
    print('Please enter a positive integer.')
elif n == 1 :
    print('Fibonacci sequence: ')
    print(n1)
else :
    print("Fibonacci sequence: ")
    print(n2)
    while (count < n):
        n3 = n1 + n2 # next fibonacci value
        print(n3, end = '\n')
        n1 = n2
        n2 = n3
        count += 1