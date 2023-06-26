length = int(input())
numbers = [0] + list(map(int, input().split()))

# 자...이걸 dp로 만들면 된다..
# def is_palindrome(start, end):
#     if start == end:
#         return 1
#     else : 
#         middle = (start+end) // 2    
#     i = 0
#     while start + i < middle+1:
#         if numbers[start+i] == numbers[end-i]:
#             i += 1
#         else:
#             return 0
#     return 1
    
# 자기 자신 위치에 palindrome이 되는 모든 번호를 기록하는건 어떨까
def find_palindrome()

for tc in range(int(input())):
    start, end = map(int, input().split())
    # print(is_palindrome(start, end))