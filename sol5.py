n_max = 100
s_max = 0

n = int(input())

coords = []

for _ in range(n):
    x,y = map(int, input().split())
    coords.append([x,y])

def s(x1,y1,x2,y2,x3,y3):
    area = abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3)) / 2
    return area

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            st = s(coords[i][0], coords[i][1],
                   coords[j][0], coords[j][1],
                   coords[k][0], coords[k][1])
            if st > s_max:
                s_max = st

result = "{0:.15f}".format(st).rstrip('0').rstrip('.')
print(result)