"""
알파벳을 숫자로 치환하기.

ABCDEFGHIJKLMNOPQRSTUVWXYZ
A = 1
B = 2
C = 3
...

"""

T = input() #테스트케이스
#T = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tmp = [(ord(i)-64) for i in T] ## 1~26까지 숫자가 담긴 리스트 생성
print(' '.join(list(map(str, tmp))))