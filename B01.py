a, b, c = input("Enter three numbers here: ").split()
a, b, c = [int(a), int(b), int(c)]
state = 0
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if ((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((b**2 + c**2) == a**2):
        state = 1
    elif (a == b) and (b == c):
        state = 2
    elif ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)):
        state = 3
    else:
        state = 5
if state == 1:
    if (a == b) or (a == c) or (b == c):
        state = 4
dic = {0: 'khong phai tam giac', 1: 'tam giac vuong', 2: 'tam giac deu', 3: 'tam giac can', 4: 'tam giac vuong can',
       5: 'tam giac thuong'}
print('day la', dic[state])