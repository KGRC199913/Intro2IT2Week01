from math import floor
n, m, a = input().split()
n, m, a = [int(n), int(m), int(a)]
row, col = 0, 0
if n%a == 0:
    row = n/a
else:
    row = floor(n/a) + 1
if m%a == 0:
    col = m/a
else:
    col = floor(m/a) + 1
print(int(row*col))
