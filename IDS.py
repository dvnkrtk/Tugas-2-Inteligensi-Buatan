from edges import edges

def dfs_terbatas(mulai, tujuan, batas, jalur, dikunjungi):
    if mulai == tujuan:
        return jalur
    if batas <= 0:
        return None

    dikunjungi.add(mulai)
    for asal, tujuan2, jarak in edges:
        tetangga = None
        if asal == mulai:
            tetangga = tujuan2
        elif tujuan2 == mulai:
            tetangga = asal
        if tetangga and tetangga not in dikunjungi:
            hasil = dfs_terbatas(tetangga, tujuan, batas - 1, jalur + [tetangga], dikunjungi)
            if hasil:
                return hasil
    dikunjungi.remove(mulai)
    return None

def ids(mulai, tujuan, max_kedalaman=50):
    for kedalaman in range(max_kedalaman):
        dikunjungi = set()
        hasil = dfs_terbatas(mulai, tujuan, kedalaman, [mulai], dikunjungi)
        if hasil:
            return hasil
    return None

if __name__ == "__main__":
    jalur = ids("Cilegon", "Banyuwangi")
    print("Jalur IDS:", jalur)
