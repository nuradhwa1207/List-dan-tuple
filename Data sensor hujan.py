#Studi Kasus: Data Sensor Hujan
data_sensor_hujan = [15, 20, 10, 5, 30, 25, 40] 
data_sensor_hujan_tuple = (15, 20, 10, 5, 30, 25, 40)

#Contoh akses elemen berdasarkan Indeks

print("Data hujan pada hari ke-3:", data_sensor_hujan[2])
print("Data hujan pada hari ke-5:", data_sensor_hujan_tuple[4])

#Contoh pemotongan data
data_minggu_pertama = data_sensor_hujan[:3]
print("Data hujan pada minggu pertama:", data_minggu_pertama)

data_minggu_terakhir = data_sensor_hujan_tuple[4:]
print("Data hujan pada minggu terakhir:", data_minggu_terakhir) 

#Contoh penggunaan perulangan
total_hujan = 0
for data in data_sensor_hujan:
    total_hujan += data
    
    rata_rata_hujan = total_hujan / len(data_sensor_hujan)
    print("Rata-rata hujan selama seminggu: ", rata_rata_hujan) 

Jumlah_hari_hujan = 0
for data in data_sensor_hujan_tuple:
    if data > 0:
        Jumlah_hari_hujan += 1

print("Jumlah hari dengan hujan:", Jumlah_hari_hujan) 