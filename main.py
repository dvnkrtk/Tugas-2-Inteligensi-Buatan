import pandas as pd
import heapq

def load_data(peta_file):
    # Baca file dengan delimiter ;
    peta_df = pd.read_csv(peta_file, delimiter=";")

    # Buat graph adjacency list
    graph = {}
    for _, row in peta_df.iterrows():
        asal, tujuan, jarak = row["Kota Asal"], row["Kota Tujuan"], int(row["Jarak Jalan"])
        if asal not in graph:
            graph[asal] = []
        if tujuan not in graph:
            graph[tujuan] = []
        graph[asal].append((tujuan, jarak))
        graph[tujuan].append((asal, jarak))  # anggap jalur 2 arah
    return graph

def ucs_search(graph, start, goal): 
    # Priority Queue dengan elemen (biaya sejauh ini, node, path)
    open_list = [(0, start, [start])]
    visited = set()

    while open_list:
        g, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)

        # Jika sampai tujuan
        if node == goal:
            return path, g

        # Kunjungi tetangga
        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + cost
                heapq.heappush(open_list, (g_new, neighbor, path + [neighbor]))

    return None, float("inf")

if __name__== "__main__":
    # Lokasi file CSV
    peta_file = "graph.csv"

    # Load data
    graph = load_data(peta_file)

    # Jalankan pencarian UCS
    start, goal = "Cilegon", "Banyuwangi"
    path, total_cost = ucs_search(graph, start, goal)

    # Tampilkan hasil
    if path:
        print("Rute terpendek dari", start, "ke", goal, ":")
        print(" -> ".join(path))
        print("Total jarak:", total_cost, "km")
    else:
        print("Tidak ditemukan jalur dari", start, "ke", goal)