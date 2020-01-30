'''
3
123 1
2737 1
32888 2
'''    
a = '12345'
a = list(a)
print(a)
a[-1], a[-2] = a[-2], a[-1]
del a[1] # index 번호로 삭제
print(a) #바뀜 확인
ans = sorted(a, reverse = True)
print(ans)