num_list = list(map(int, input().split(', ')))

def print_square(n1, n2):
    print(f'{n1} => {n1**2}')
    print(f'{n2} => {n2**2}')

print_square(num_list[0], num_list[1])