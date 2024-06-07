def f(s): 
    answer = left = right = 0
    data = set()
    while right < len(s): 
        c = s[right]
        if c not in data:      
            data.add(c)
            answer = max(answer, right-left+1)
            right += 1
        else: 
            while c in data: 
                data.remove(s[left])
                left += 1
    return answer


s = 'abcbdbefg'
print(f(s))
# определяют максимальную подстроку, состоящую из разных букв