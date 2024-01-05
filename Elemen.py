# Mengakses elemen menggunakan indeks
names = ["Alice", "Bob", "Charlie", "David"]
print(names[2])

fruits = ("apple", "banana", "orange")
print(fruits[0])

#Teknik pemotongan (slicing) 
cities = ["New York", "Los Angeles", "Chicago", "Houston"]
print(cities[1:3])
colors = ("red", "green", "blue")
print(colors[0:2])


#Penggunaan perulangan (loop)
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x)

coordinates = (10.0, 20.5)
total = 0
for n in coordinates:
    total += n 
print("Koordinat: ", total)