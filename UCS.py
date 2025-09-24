import heapq
from edges import edges

def ucs(mulai, tujuan):
    antrian = [(0, [mulai])]   # (biaya, jalur)
    dikunjungi = set()

    while antrian:
        biaya, jalur = heapq.heappop(antrian)
        kota = jalur[-1]

        if kota == tujuan:
            return jalur, biaya

        if kota not in dikunjungi:
            dikunjungi.add(kota)
            for asal, tujuan2, jarak in edges:
                if asal == kota and tujuan2 not in dikunjungi:
                    heapq.heappush(antrian, (biaya + jarak, jalur + [tujuan2]))
                elif tujuan2 == kota and asal not in dikunjungi:
                    heapq.heappush(antrian, (biaya + jarak, jalur + [asal]))

    return None, float("inf")

if __name__ == "__main__":
    jalur, biaya = ucs("Cilegon", "Banyuwangi")
    print("Jalur UCS:", jalur, "Biaya:", biaya)
