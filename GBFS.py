import heapq
from edges import edges
from heuristics import heuristics

def h(n):
    for city, val in heuristics:
        if city == n:
            return val
    return float("inf")

def gbfs(start, goal):
    queue = [(h(start), start, [start])]
    visited = set()

    while queue:
        _, node, path = heapq.heappop(queue)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)

        for u, v, w in edges:
            if u == node and v not in visited:
                heapq.heappush(queue, (h(v), v, path+[v]))
            elif v == node and u not in visited:
                heapq.heappush(queue, (h(u), u, path+[u]))
    return None

if __name__ == "__main__":
    path, cost = gbfs("Cilegon", "Banyuwangi")
    print("GBFS Path:", path)
    print("GBFS Cost:", cost)
