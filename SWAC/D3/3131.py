# input 없음

max_num = 20 # 100만
prime_num = [2,3,5,7]

# tmp = [False] + [True for _ in range(2, max_num-1)] # 100만개의 0을 만들고


## prime check
# ver. 1) 무식하게 하기
# def isPrime_bad(num):
#     prime_num = [2, 3]
#     n = 4
#     if num == 1:
#         return False

#     # 절반이상 단축 가능
#     for p in prime_num:
#         if num % p is 0:
#             return False
#     else:

# 입력받는 수를 n이라고 할 때,
# n = a*b 로 표현할 수 있다면 소수가 아니다.
# 그럼 a의 최대값은 round(n**0.5)+1 까지.

# 에라토스테네스의 체
def Num_underPrime(num):
    arr = [False] + [True for _ in range(num)] # num+1 길이의 arr 생성
    n = 1
    prime_num = [2,3]
    while n <= num : 
        if n == 1:
            arr[n] = False
        elif n % 2 is 0:
            arr[n] = False
        elif n % 3 is 0:
            arr[n] = False
        elif arr[n] == True:
            prime_num.append(n)
            arr[n::n] = [False] * (num//n)
        n += 1
    return prime_num

print(' '.join(map(str, Num_underPrime(max_num))))
