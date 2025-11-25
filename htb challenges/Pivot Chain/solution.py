import heapq
import sys

# initial data
target_string = input()
target_list = target_string.split()
hosts_number = int(target_list[0])
paths_number = int(target_list[1])
source = int(target_list[2].split('_')[1])-1  # numbering from 0
target = int(target_list[3].split('_')[1])-1  # numbering from 0

# parse paths
paths = []
for _ in range(hosts_number):
    paths.append([])

for _ in range(paths_number):
    path = input().split()
    starting_point = int(path[0].split('_')[1])-1
    target_and_distance = [int(path[1].split('_')[1])-1, int(path[2])]  # numbering from 0
    paths[starting_point].append(target_and_distance)


# calculates distances to all hosts: performance O(V²) and no early break
def dijkstra_all(neighbouring_list, starting_host) -> list:
    hosts_num = len(neighbouring_list)

    d = [sys.maxsize] * hosts_num
    p = [-1] * hosts_num
    visited = [False] * hosts_num

    d[starting_host] = 0

    for _ in range(hosts_num):
        # Find the unvisited vertex with the smallest distance
        u = -1
        for i in range(hosts_num):
            if not visited[i] and (u == -1 or d[i] < d[u]):
                u = i

        if u == -1:
            break  # No reachable vertices left

        visited[u] = True

        # Relax edges
        for v, distance in neighbouring_list[u]:
            if not visited[v] and d[u] + distance < d[v]:
                d[v] = d[u] + distance
                p[v] = u

    return d


# calculates distance to target host only - early break
def dijkstra_target(neighbouring_list, starting_host, destination) -> list:
    hosts_num = len(neighbouring_list)

    d = [sys.maxsize] * hosts_num
    p = [-1] * hosts_num
    visited = [False] * hosts_num

    d[starting_host] = 0

    for _ in range(hosts_num):
        # Get closest unvisited vertex
        u = -1
        for i in range(hosts_num):
            if not visited[i] and (u == -1 or d[i] < d[u]):
                u = i

        if u == -1:
            break

        # early stop: destination reached
        if u == destination:
            break

        visited[u] = True

        # relax edges
        for v, distance in neighbouring_list[u]:
            if not visited[v] and d[u] + distance < d[v]:
                d[v] = d[u] + distance
                p[v] = u

    return d


# version using a priority queue improves performance from O(V²) to O(E logV)
def dijkstra_fast(neighbouring_list, start, destination) -> list:
    hosts_num = len(neighbouring_list)

    d = [sys.maxsize] * hosts_num
    p = [-1] * hosts_num
    visited = [False] * hosts_num

    d[start] = 0
    pq = [(0, start)]   # (distance, node)

    while pq:
        # pop and return the smallest item from the heap pq, maintaining the min-heap invariant
        dist_u, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True

        # early stop: destination reached
        if u == destination:
            break

        for v, distance in neighbouring_list[u]:
            if not visited[v] and dist_u + distance < d[v]:
                d[v] = dist_u + distance
                p[v] = u
                # push the value v onto the heap d[v], maintaining the min-heap invariant
                heapq.heappush(pq, (d[v], v))

    return d


print(dijkstra_fast(paths, source, target)[target])
