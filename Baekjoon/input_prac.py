'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
    
import sys
T = int(input())

for _ in range(T):
    tmp = list(sys.stdin.readline())
    print(tmp)
'''
numbers = [
    [1, 2, 3],
    [2, 2, 2],
    [3, 2, 1],
]

for i in range(3):
    for j in range(3):
        # print(numbers[j][i])
        continue

def func(a, b=1, c=2, *args, **kwargs):
    d = sum([n*2 for n in args if n>2])
    e = sum([v**2 for v in kwargs.values()])
    print(a, b, c, d, e)
    return a + b + c + d + e

def my_func1(n):
    return n**3

def my_func2(n):
    return n%2

numbers = [1,2,3]

new_numbers = list(filter(my_func2, map(my_func1, numbers)))
name = '1111'
word = 'python'

print(word[3:8])