from ucs import ucs
from ids import ids
from gbfs import gbfs
from a_star import a_star

mulai = "Cilegon"
tujuan = "Banyuwangi"

jalur_ucs, biaya_ucs = ucs(mulai, tujuan)
jalur_ids, biaya_ids = ids(mulai, tujuan)
jalur_gbfs, biaya_gbfs = gbfs(mulai, tujuan)
jalur_astar, biaya_astar = a_star(mulai, tujuan)

print("=== Hasil Pencarian Rute ===\n")
print("UCS   :", " -> ".join(jalur_ucs), "| Biaya:", biaya_ucs)
print("IDS   :", " -> ".join(jalur_ids), "| Biaya:", biaya_ids)
print("GBFS  :", " -> ".join(jalur_gbfs), "| Biaya:", biaya_gbfs)
print("A*    :", " -> ".join(jalur_astar), "| Biaya:", biaya_astar)
