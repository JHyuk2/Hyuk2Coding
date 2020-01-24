"""
- 출력하기 -

#++++
+#+++
++#++
+++#+
++++#

"""

for i in range(5):
    tmp = ''
    for j in range(5):
        if j == i:
            tmp += '#'
        else:
            tmp += '+'
            
    print(tmp)