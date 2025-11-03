# Implementasi sederhana Algoritma A* untuk pengambilan keputusan organisasi besar

# Struktur data graph disimpan dalam dictionary
graph = {
    'Mulai': {'Analisis': 3, 'Pilih Vendor': 10},
    'Analisis': {'Pilih Vendor': 5, 'Budget Approve': 9},
    'Pilih Vendor': {'Negosiasi': 2},
    'Negosiasi': {'Uji Coba': 4},
    'Uji Coba': {'Implementasi': 3},
    'Implementasi': {'Selesai': 1},
    'Budget Approve': {'Implementasi': 8}
}

# Heuristik (perkiraan jarak/biaya ke tujuan)
# Semakin kecil nilai, semakin dekat ke "Selesai"
h = {
    'Mulai': 10,
    'Analisis': 8,
    'Pilih Vendor': 6,
    'Negosiasi': 5,
    'Uji Coba': 3,
    'Budget Approve': 4,
    'Implementasi': 1,
    'Selesai': 0
}

def a_star(start, goal):
    open_nodes = {start}          # node yang akan dievaluasi
    previous = {}                 # menyimpan jalur terbaik
    g = {start: 0}                # g(n): biaya aktual dari start ke node
    f = {start: h[start]}         # f(n): total biaya perkiraan (g + h)

    while open_nodes:  # ← benar, sejajar dengan kode di atasnya
        current = min(open_nodes, key=lambda x: f.get(x, float('inf')))
        if current == goal:
            # rekonstruksi jalur
            path = []
            while current in previous:
                path.append(current)
                current = previous[current]
            path.append(start)
            path.reverse()
            return path, g[goal]

        open_nodes.remove(current)

        # jelajahi tetangga node saat ini
        for neighbor, cost in graph.get(current, {}).items():
           tentative_g = g[current] + cost  # hitung g(n)

           if tentative_g < g.get(neighbor, float('inf')):
                previous[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + h[neighbor]  # f(n) = g(n) + h(n)
                open_nodes.add(neighbor)

    return None, float('inf')  # tidak ada jalur ditemukan


# Jalankan algoritma
start_node = 'Mulai'
goal_node = 'Selesai'

path, total_cost = a_star(start_node, goal_node)

print("=== HASIL KEPUTUSAN ORGANISASI ===")
if path:
    print("Jalur terbaik :", " -> ".join(path))
    print("Total biaya :", total_cost)
else:
    print("Tidak ada jalur ditemukan.")

