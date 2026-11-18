"""Program utama Game Score Analyzer.

Jalankan program dengan perintah:
    python main.py
"""

from statistik_game import (
    buat_leaderboard,
    cari_pemain_tertinggi,
    cari_skor_terendah,
    cari_skor_tertinggi,
    hitung_rata_rata_skor,
    hitung_total_skor,
    klasifikasi_level,
)


def format_skor(skor):
    """Mengubah angka menjadi format skor yang mudah dibaca."""
    return f"{skor:,.0f}".replace(",", ".")


def tampilkan_data_pemain(data_pemain):
    """Menampilkan seluruh data pemain."""
    print("\n" + "=" * 56)
    print("DAFTAR PEMAIN")
    print("=" * 56)

    if not data_pemain:
        print("Belum ada data pemain.")
        return

    for nomor, pemain in enumerate(data_pemain, start=1):
        print(
            f"{nomor:>2}. {pemain['nama']:<20} "
            f"Skor: {format_skor(pemain['skor']):>8} "
            f"| Level: {klasifikasi_level(pemain['skor'])}"
        )


def tampilkan_ringkasan(data_pemain):
    """Menampilkan ringkasan statistik permainan."""
    print("\n" + "=" * 56)
    print("RINGKASAN STATISTIK GAME")
    print("=" * 56)

    if not data_pemain:
        print("Tidak ada data untuk dihitung.")
        return

    pemain_tertinggi = cari_pemain_tertinggi(data_pemain)
    rata_rata = hitung_rata_rata_skor(data_pemain)

    print("Jumlah pemain       :", len(data_pemain))
    print("Total seluruh skor  :", format_skor(hitung_total_skor(data_pemain)))
    print("Rata-rata skor      :", format_skor(rata_rata))
    print("Skor terendah       :", format_skor(cari_skor_terendah(data_pemain)))
    print("Skor tertinggi      :", format_skor(cari_skor_tertinggi(data_pemain)))
    print(
        "Pemain terbaik      :",
        pemain_tertinggi["nama"],
        f"({format_skor(pemain_tertinggi['skor'])} poin)"
    )


def tampilkan_leaderboard(data_pemain):
    """Menampilkan peringkat pemain berdasarkan skor."""
    print("\n" + "=" * 56)
    print("LEADERBOARD PEMAIN")
    print("=" * 56)

    leaderboard = buat_leaderboard(data_pemain)

    if not leaderboard:
        print("Belum ada pemain untuk ditampilkan.")
        return

    print(f"{'Rank':<8}{'Nama Pemain':<22}{'Skor':>12}  {'Level'}")
    print("-" * 56)

    for pemain in leaderboard:
        print(
            f"{pemain['peringkat']:<8}"
            f"{pemain['nama']:<22}"
            f"{format_skor(pemain['skor']):>12}  "
            f"{pemain['level']}"
        )


def tambah_pemain(data_pemain):
    """Menerima nama dan skor pemain baru dari pengguna."""
    print("\nTAMBAH PEMAIN BARU")

    nama = input("Nama pemain: ").strip()
    if not nama:
        print("Nama pemain tidak boleh kosong.")
        return

    input_skor = input("Skor pemain: ").strip()

    try:
        skor = int(input_skor)
        if skor < 0:
            print("Skor tidak boleh negatif.")
            return
    except ValueError:
        print("Skor harus berupa bilangan bulat.")
        return

    data_pemain.append({
        "nama": nama,
        "skor": skor
    })

    print(f"Data pemain {nama} berhasil ditambahkan.")


def tampilkan_demo_klasifikasi():
    """Menunjukkan contoh batas klasifikasi level pemain."""
    print("\n" + "=" * 56)
    print("DEMO KLASIFIKASI LEVEL")
    print("=" * 56)

    daftar_uji = [0, 450, 500, 950, 1000, 1750, 2000, 2500]

    for skor in daftar_uji:
        print(f"Skor {format_skor(skor):>5} -> {klasifikasi_level(skor)}")


def main():
    """Menjalankan menu utama aplikasi."""
    data_pemain = [
        {"nama": "Raka", "skor": 2450},
        {"nama": "Nadia", "skor": 1800},
        {"nama": "Bima", "skor": 1250},
        {"nama": "Sinta", "skor": 950},
        {"nama": "Doni", "skor": 450},
    ]

    while True:
        print("\n" + "=" * 56)
        print("             GAME SCORE ANALYZER")
        print("=" * 56)
        print("1. Lihat daftar pemain")
        print("2. Lihat ringkasan statistik")
        print("3. Lihat leaderboard")
        print("4. Tambah pemain")
        print("5. Demo klasifikasi level")
        print("0. Keluar")
        print("-" * 56)

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            tampilkan_data_pemain(data_pemain)
        elif pilihan == "2":
            tampilkan_ringkasan(data_pemain)
        elif pilihan == "3":
            tampilkan_leaderboard(data_pemain)
        elif pilihan == "4":
            tambah_pemain(data_pemain)
        elif pilihan == "5":
            tampilkan_demo_klasifikasi()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan Game Score Analyzer.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih menu 0 sampai 5.")


if __name__ == "__main__":
    main()
