import heapq
from edges import edges
from heuristics import heuristics

def astar(mulai, tujuan):
    antrian = [(heuristics[mulai], 0, [mulai])]  # (f, g, jalur)
    dikunjungi = set()

    while antrian:
        f, g, jalur = heapq.heappop(antrian)
        kota = jalur[-1]

        if kota == tujuan:
            return jalur, g

        if kota not in dikunjungi:
            dikunjungi.add(kota)
            for asal, tujuan2, jarak in edges:
                tetangga = None
                if asal == kota:
                    tetangga = tujuan2
                elif tujuan2 == kota:
                    tetangga = asal
                if tetangga and tetangga not in dikunjungi:
                    g_baru = g + jarak
                    f_baru = g_baru + heuristics[tetangga]
                    heapq.heappush(antrian, (f_baru, g_baru, jalur + [tetangga]))
    return None, float("inf")

if __name__ == "__main__":
    jalur, biaya = astar("Cilegon", "Banyuwangi")
    print("Jalur A*:", jalur, "Biaya:", biaya)
