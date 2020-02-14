def solution(heights):
    length = len(heights)
    res = []
    
    for i in range(length):
        stack = heights[:i+1]
        if i == 0:
            res.append(i)
        else:
            while bool(stack):
                if stack.pop() > heights[i]:
                    res.append(len(stack)+1)
                    break
                else:
                    continue
            else:
                res.append(0)
    return res
                
