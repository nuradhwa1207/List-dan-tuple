
# Program Mengetahui Ujian

# Menggetahui biodata mahasiswa menggunakan list
biodata = ["Nur Adhwa", 12, 7, 2005, "Penajam", 18, "Semester 1"]
print("Nama: ", biodata[0])
print("Tanggal Lahir: ", biodata[1])
print("Bulan Lahir: ", biodata[2])
print("Tahun Lahir: ", biodata[3])
print("Asal Daerah: ", biodata[4])
print("Umur: ",biodata[5])
print("Kelas: ", biodata[6])

# Membuat jadwal Ujian
tanggal = (17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
            12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)

print("Tanggal Quiz: ", tanggal[15:22])
print("Tanggal Ujian: ", tanggal[:7])
