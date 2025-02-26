s = open('24-309.txt').readline()
# s='SSFSRQRRFSRQ'
s = s.replace('FSRQ', 'FSR SRQ').split()
m = 0
for i in range(len(s)):
    c = ''.join(s[i:i + 81])
    m = max(m, len(c) - 160)
print(m)
