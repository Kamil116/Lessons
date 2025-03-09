# Решение Риты
f = open('24.txt')
s = f.read()
mx = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == '78':
        sm = 0
        a = 78
        for r in range(i + 2, len(s) - 1, 2):
            if s[r] + s[r + 1] == '99':
                sm += 2
                a += 1
                for r3 in range(r + 2, len(s) - 2, 3):
                    if s[r3] + s[r3 + 1] + s[r3 + 2] == str(a + 1):
                        a += 1
                        sm += 3
                    else:
                        break
                break
            if s[r] + s[r + 1] == str(a + 1):
                a += 1
                sm += 2
            else:
                break
        a = 78
        for l in range(i - 2, -1, -2):
            if s[l] + s[l + 1] == str(a - 1):
                a -= 1
                sm += 2
            else:
                break
        mx = max(sm, mx)
print(mx + 2)
