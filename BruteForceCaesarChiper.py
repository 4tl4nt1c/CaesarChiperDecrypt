def caesar_decrypt(text, shift):
    hasil = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            kode_baru = (ord(char) - base - shift) % 26 + base
            hasil += chr(kode_baru)
        else:
            hasil += char
    return hasil

def hitung_kecocokan(teks, kata_umum):
    teks_lower = teks.lower()
    return sum(1 for kata in kata_umum if kata in teks_lower)

if __name__ == "__main__":
    ciphertext = input("Masukkan teks terenkripsi: ")

    kata_umum = ["aku", "kamu", "ini", "yang", "saya", "dan","mereka","jahat","baru","lama","senang","kapan","jatuh","tiba","suka","sayang","selamat","berhasil", "dia", "kita", "jangan"]

    kemungkinan_terbaik = ""
    jumlah_kecocokan_tertinggi = 0
    shift_terbaik = 0

    for shift in range(1, 26):
        hasil = caesar_decrypt(ciphertext, shift)
        cocok = hitung_kecocokan(hasil, kata_umum)

        if cocok > jumlah_kecocokan_tertinggi:
            jumlah_kecocokan_tertinggi = cocok
            kemungkinan_terbaik = hasil
            shift_terbaik = shift

    if jumlah_kecocokan_tertinggi > 0:
        print(f"\n🔓 Hasil dekripsi terbaik (Shift {shift_terbaik}):")
        print(kemungkinan_terbaik)
    else:
        print("\n❌ Gagal menemukan kata umum. Mohon cari secara manual:")

        for shift in range(1, 26):
            hasil = caesar_decrypt(ciphertext, shift)
            print(f"[Shift {shift:2}] {hasil}")
