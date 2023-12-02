# 1~100 
# 3:Fizz, 5:Buzz, 15:FizzBuzz

# 演習2

for i in range(1, 101):
    if i % 15 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('{}: FizzBuzz'.format(i))
    elif i % 3 == 0:
        print('{}: Fizz'.format(i))
    elif i % 5 == 0:
        print('{}: Buzz'.format(i))
    else:
        print(i)