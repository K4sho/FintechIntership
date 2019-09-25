x1,y1,x2,y2 = map(int, input().split())

delta_x = abs(x2 - x1)
delta_y = abs(y2 - y1)


while delta_x != 0 and delta_y != 0:
    if delta_x > delta_y:
        delta_x %= delta_y
    else:
        delta_y %= delta_x

n = delta_x + delta_y

dx = (x2 - x1) / n
dy = (y2 - y1) / n

list_of_pair = []
for i in range(0, n+1):
    list_of_pair.append((x1 + dx*i, y1 + dy*i))

print(len(list_of_pair))