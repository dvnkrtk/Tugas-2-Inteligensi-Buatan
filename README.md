# Pencarian Rute Tercepat: Cilegon → Banyuwangi

## Identitas Kelompok
- Devina Kartika       - 123140036
- Awi Septian Prasetyo - 123140201
- Muhammad Bimastiar   - 123140221

---

## Representasi Graf
Graf dibentuk dari data **kota asal, kota tujuan, dan jarak antar kota**.  
- Simpul (node) = nama kota  
- Sisi (edge) = jalan yang menghubungkan kota  
- Bobot (weight) = jarak antar kota (dalam kilometer)  

Selain itu terdapat **data heuristik (h(n))**, yaitu estimasi jarak dari suatu kota ke kota tujuan **Banyuwangi**.  
Data graf tersimpan pada file `edges.py` dan data heuristik pada file `heuristics.py`.

---

## Metode Searching

### 1. Uniform Cost Search (UCS)
- Termasuk **uninformed search**.  
- Prinsip: selalu memilih jalur dengan **biaya total terkecil** sejauh ini.  
- **Kelebihan:** pasti menemukan solusi optimal.  
- **Kekurangan:** bisa memakan waktu jika graf sangat besar.  
- Implementasi: file [`ucs.py`](ucs.py).

---

### 2. Iterative Deepening Search (IDS)
- Kombinasi antara **DFS** dan **Batas Kedalaman**.  
- Prinsip: mencari dengan DFS, tapi kedalaman dibatasi (mulai dari 1, 2, 3, dst).  
- **Kelebihan:** hemat memori seperti DFS, tetapi tetap lengkap.  
- **Kekurangan:** ada pengulangan pencarian di level atas.  
- Implementasi: file [`ids.py`](ids.py).

---

### 3. Greedy Best-First Search (GBFS)
- Termasuk **informed search**.  
- Prinsip: memilih simpul dengan nilai heuristik **h(n) terkecil** (paling dekat ke goal menurut estimasi).  
- **Kelebihan:** cepat sampai tujuan.  
- **Kekurangan:** solusi tidak selalu optimal.  
- Implementasi: file [`gbfs.py`](gbfs.py).

---

### 4. A* Search
- Termasuk **informed search**.  
- Prinsip: menggunakan fungsi evaluasi:
- `g(n)` = biaya dari titik awal sampai simpul n  
- `h(n)` = estimasi biaya dari n ke goal  
- **Kelebihan:** efisien dan optimal jika heuristik admissible.  
- **Kekurangan:** butuh memori lebih banyak.  
- Implementasi: file [`astar.py`](astar.py).

---

## Struktur Folder
project/
├─ README.md
├─ a_star.py
├─ gbfs.py
├─ ids.py
├─ main.py
├─ ucs.py
├─ edges.py
├─ heuristics.py

