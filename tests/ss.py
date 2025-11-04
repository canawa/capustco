s = str(input())
for i in range(0,len(s)):
    p = s
    p = p.replace(p[i],'', 1)
    if p == p[::-1]:
        print(p)
        print(i)
        break