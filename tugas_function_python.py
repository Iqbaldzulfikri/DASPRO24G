
# Function 1: Membalik setiap kata dalam kalimat tanpa mengubah urutan kata
def reverse_per_kata(kalimat):
    kata_kata = kalimat.split()  # Memisahkan kalimat menjadi list kata
    hasil = []
    for kata in kata_kata:
        hasil.append(kata[::-1])  # Membalik tiap kata
    return " ".join(hasil)  # Menggabungkan kembali menjadi kalimat


# Function 2: Mengurutkan kata-kata dalam kalimat berdasarkan indeks yang diberikan
def urutkan_kalimat(kalimat, urutan):
    kata_kata = kalimat.split()  # Memisahkan kalimat menjadi list kata
    hasil = [""] * len(urutan)  # Menyiapkan list kosong untuk hasil
    for i in range(len(urutan)):
        hasil[i] = kata_kata[urutan[i]-1]  # Mengisi hasil dengan kata berdasarkan urutan (dimulai dari 1)
    return " ".join(hasil)  # Menggabungkan kembali menjadi kalimat


# Function 3: Mengganti huruf vokal berdasarkan opsi
# Opsi 1 = vokal kecil, Opsi 2 = vokal kapital
def ganti_vokal(kalimat, opsi):
    hasil = ""
    for huruf in kalimat:
        if opsi == 1:  # Ganti vokal kecil
            if huruf == 'a':
                hasil += '4'
            elif huruf == 'i':
                hasil += '1'
            elif huruf == 'u':
                hasil += '|_|'
            elif huruf == 'e':
                hasil += '3'
            elif huruf == 'o':
                hasil += '0'
            else:
                hasil += huruf
        elif opsi == 2:  # Ganti vokal kapital
            if huruf == 'A':
                hasil += '4'
            elif huruf == 'I':
                hasil += '1'
            elif huruf == 'U':
                hasil += '|_|'
            elif huruf == 'E':
                hasil += '3'
            elif huruf == 'O':
                hasil += '0'
            else:
                hasil += huruf
    return hasil


# Bagian uji coba (dijalankan hanya untuk menunjukkan hasil)
print(reverse_per_kata("AKU CINTA KAMU"))  # Output: "UKA ATNIC UMAK"

print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))  # Output: "PYTHON HARI BELAJAR SEDANG INI"

print(ganti_vokal("Aku Cinta Kamu", 1))  # Output: "Ak|_| C1nt4 K4m|_|"

print(ganti_vokal("Aku Cinta Kamu", 2))  # Output: "4ku Cinta K4mu"
