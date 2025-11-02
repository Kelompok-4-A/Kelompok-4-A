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
heuristic = {
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
    open_set = {start}                # node yang akan dievaluasi
    came_from = {}                    # menyimpan jalur terbaik
    g_score = {start: 0}              # biaya aktual dari start ke node
    f_score = {start: heuristic[start]}  # perkiraan total biaya (g + h)

    while open_set:
        # ambil node dengan nilai f_score terkecil
        current = min(open_set, key=lambda x: f_score.get(x, float('inf')))

        if current == goal:
            # rekonstruksi jalur
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        open_set.remove(current)

        # jelajahi tetangga node saat ini
        for neighbor, cost in graph.get(current, {}).items():
            tentative_g = g_score[current] + cost

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                open_set.add(neighbor)

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
