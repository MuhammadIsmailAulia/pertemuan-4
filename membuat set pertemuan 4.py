# 1. Membuat set (menggunakan kurung kurawal {})
angka = {1, 2, 3, 4, 5, 5, 5} # Angka 5 yang diduplikat akan otomatis dihapus
print(f"Set awal: {angka}") # output: {1, 2, 3, 4, 5}
# 2. Menambah Data
angka.add(6) #Menghapus angka 1
angka.update([7, 8]) #Menambha banyak item sekaligus
print(f"setelah ditambah: {angka}")
# 4. Operasi Himpunan (MAtematika)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Gabungan (union)
print(f"Gabungan: {set_a | set_b}") # output: {1, 2, 3, 4, 5}
# Irisan (Intersection)
print(f"Irisan: {set_a & set_b}") # output: {3}
# Selisih (Difference)
print(f"Selisih A-B: {set_a - set_b}") #output: {1, 2}
