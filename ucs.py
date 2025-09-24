import heapq
from edges import edges

def get_neighbors(node):
    hasil = []
    for awal, akhir, biaya in edges:
        if awal == node:
            hasil.append((akhir, biaya))
        elif akhir == node:
            hasil.append((awal, biaya))
    return hasil

def ucs(start, goal):
    heap = [(0, [start])]
    visited = set()
    
    while heap:
        biaya, path = heapq.heappop(heap)
        node = path[-1]
        if node == goal:
            return path, biaya
        if node in visited:
            continue
        visited.add(node)
        for tetangga, c in get_neighbors(node):
            if tetangga not in path:
                heapq.heappush(heap, (biaya + c, path + [tetangga]))
    return None, float('inf')
