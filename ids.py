from edges import edges

def dfs_terbatas(mulai, goal, batas, jalur):
    if mulai == goal:
        return jalur
    if batas == 0:
        return None
    for asal, tujuan, _ in edges:
        if asal == mulai and tujuan not in jalur:
            hasil = dfs_terbatas(tujuan, goal, batas - 1, jalur + [tujuan])
            if hasil:
                return hasil
        elif tujuan == mulai and asal not in jalur:
            hasil = dfs_terbatas(asal, goal, batas - 1, jalur + [asal])
            if hasil:
                return hasil
    return None

def ids(mulai, goal, max_batas=50):
    for batas in range(max_batas):
        hasil = dfs_terbatas(mulai, goal, batas, [mulai])
        if hasil:
            biaya = 0
            for i in range(len(hasil)-1):
                for a, b, c in edges:
                    if (a == hasil[i] and b == hasil[i+1]) or (b == hasil[i] and a == hasil[i+1]):
                        biaya += c
            return hasil, biaya
    return None, float('inf')
