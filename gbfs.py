import heapq
from edges import edges
from heuristics import nilai_heuristik

def get_neighbors(node):
    hasil = []
    for awal, akhir, biaya in edges:
        if awal == node:
            hasil.append((akhir, biaya))
        elif akhir == node:
            hasil.append((awal, biaya))
    return hasil

def gbfs(start, goal):
    heap = [(nilai_heuristik(start), [start])]
    visited = set()
    
    while heap:
        _, path = heapq.heappop(heap)
        node = path[-1]
        if node == goal:
            biaya = 0
            for i in range(len(path)-1):
                for a, b, c in edges:
                    if (a == path[i] and b == path[i+1]) or (b == path[i] and a == path[i+1]):
                        biaya += c
            return path, biaya
        if node in visited:
            continue
        visited.add(node)
        for tetangga, _ in get_neighbors(node):
            if tetangga not in path:
                heapq.heappush(heap, (nilai_heuristik(tetangga), path + [tetangga]))
    return None, float('inf')
