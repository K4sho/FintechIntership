from itertools import chain, groupby

n = int(input())

matrix = [[int(j) for j in input().split()] for i in range(n)]

#n = 3
#matrix = [[0, 1, 1],
#          [1, 0, 0],
#          [1, 1, 0]]

list_of_pairs = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            list_of_pairs.append((i+1, j+1))

graph = {}

for k, it in groupby(sorted(list_of_pairs), key=lambda x: x[0]):
    graph[k] = {e for _, e in it}

sub_graph = {}
while True:
    vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
    sub_graph = {k: vertex_set & vs for k, vs in graph.items()
                 if k in vertex_set and vertex_set & vs}

    if sub_graph == graph:
        break
    else:
        graph = sub_graph

# Если есть подграф то он цикличен
print(1 if graph else 0)