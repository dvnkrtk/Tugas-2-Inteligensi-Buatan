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

def a_star(start, goal):
    heap = [(nilai_heuristik(start), 0, [start])]
    visited = set()
    
    while heap:
        f, g, path = heapq.heappop(heap)
        node = path[-1]
        if node == goal:
            return path, g
        if node in visited:
            continue
        visited.add(node)
        for tetangga, c in get_neighbors(node):
            if tetangga not in path:
                g_baru = g + c
                f_baru = g_baru + nilai_heuristik(tetangga)
                heapq.heappush(heap, (f_baru, g_baru, path + [tetangga]))
    return None, float('inf')
