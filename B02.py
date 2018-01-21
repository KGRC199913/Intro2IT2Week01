last_mont, this_month = input("nhap vao chi so dien thang truoc roi toi chi so thang nay:\n").split()
last_mont, this_month = [int(last_mont), int(this_month)]
delta_consume = this_month - last_mont
if 0 < delta_consume < 51:
    unit_price = 1.549
elif 50 < delta_consume < 101:
    unit_price = 1.600
elif 100 < delta_consume < 201:
    unit_price = 1.858
elif 200 < delta_consume < 301:
    unit_price = 2.340
elif 300 < delta_consume < 401:
    unit_price = 2.615
elif 400 < delta_consume:
    unit_price = 2.701
print('tien dien sinh hoat thang nay la', (unit_price * delta_consume) * 10/100)


