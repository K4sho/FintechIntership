n = int(input())
list_of_clients = []

for _ in range(n):
    hours, mins = map(int, input().split())
    list_of_clients.append([hours, mins])

list_of_out_clients = []

for h, m in list_of_clients:
    m_out = m + 30
    if m_out >= 60:
        delta = m_out - 60
        h_out = h + 1
        if h_out > 23:
            h_out = 0
        m_out = delta
    else:
        h_out = h
    list_of_out_clients.append([h_out, m_out])

for h, m in list_of_out_clients:
    print(h, m)