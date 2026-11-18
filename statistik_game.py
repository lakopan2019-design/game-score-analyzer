"""Modul fungsi statistik untuk Game Score Analyzer.

Modul ini menyediakan fungsi reusable untuk mengolah skor pemain game:
validasi data, total, rata-rata, skor tertinggi/terendah, leaderboard,
dan klasifikasi level pemain.
"""

from math import isfinite


def validasi_data_pemain(data_pemain):
    """Memastikan data pemain memiliki format dan skor yang valid.

    Format setiap pemain:
        {"nama": "Raka", "skor": 1200}

    Raises:
        TypeError: Jika struktur atau tipe data tidak sesuai.
        ValueError: Jika nama kosong atau skor negatif/tidak valid.
    """
    if not isinstance(data_pemain, (list, tuple)):
        raise TypeError("Data pemain harus berupa list atau tuple.")

    for nomor, pemain in enumerate(data_pemain, start=1):
        if not isinstance(pemain, dict):
            raise TypeError(f"Data pemain ke-{nomor} harus berupa dictionary.")

        nama = pemain.get("nama")
        skor = pemain.get("skor")

        if not isinstance(nama, str) or not nama.strip():
            raise ValueError(f"Nama pemain ke-{nomor} tidak boleh kosong.")

        if isinstance(skor, bool) or not isinstance(skor, (int, float)):
            raise TypeError(f"Skor pemain ke-{nomor} harus berupa angka.")

        if not isfinite(skor) or skor < 0:
            raise ValueError(f"Skor pemain ke-{nomor} harus angka positif atau nol.")

    return data_pemain


def hitung_total_skor(data_pemain):
    """Menghitung total skor seluruh pemain."""
    validasi_data_pemain(data_pemain)
    return sum(pemain["skor"] for pemain in data_pemain)


def hitung_rata_rata_skor(data_pemain):
    """Menghitung rata-rata skor. Mengembalikan None jika data kosong."""
    validasi_data_pemain(data_pemain)

    if len(data_pemain) == 0:
        return None

    return hitung_total_skor(data_pemain) / len(data_pemain)


def cari_skor_terendah(data_pemain):
    """Mengembalikan skor terendah, atau None jika data kosong."""
    validasi_data_pemain(data_pemain)

    if len(data_pemain) == 0:
        return None

    return min(pemain["skor"] for pemain in data_pemain)


def cari_skor_tertinggi(data_pemain):
    """Mengembalikan skor tertinggi, atau None jika data kosong."""
    validasi_data_pemain(data_pemain)

    if len(data_pemain) == 0:
        return None

    return max(pemain["skor"] for pemain in data_pemain)


def cari_pemain_tertinggi(data_pemain):
    """Mengembalikan data pemain dengan skor tertinggi.

    Jika ada lebih dari satu pemain dengan skor tertinggi yang sama,
    fungsi mengembalikan pemain pertama yang ditemukan.
    """
    validasi_data_pemain(data_pemain)

    if len(data_pemain) == 0:
        return None

    return max(data_pemain, key=lambda pemain: pemain["skor"])


def klasifikasi_level(skor):
    """Mengklasifikasikan level pemain berdasarkan skor.

    Aturan:
        0-499       : Pemula
        500-999     : Bronze
        1000-1999   : Silver
        2000 ke atas: Gold
    """
    if isinstance(skor, bool) or not isinstance(skor, (int, float)):
        raise TypeError("Skor harus berupa angka.")

    if not isfinite(skor) or skor < 0:
        raise ValueError("Skor harus berupa angka positif atau nol.")

    if skor >= 2000:
        return "Gold"
    elif skor >= 1000:
        return "Silver"
    elif skor >= 500:
        return "Bronze"
    else:
        return "Pemula"


def buat_leaderboard(data_pemain):
    """Membuat leaderboard dari skor tertinggi ke terendah.

    Pemain dengan skor sama memperoleh peringkat yang sama.
    Contoh peringkat: 1, 1, 3.
    """
    validasi_data_pemain(data_pemain)

    pemain_urut = sorted(
        data_pemain,
        key=lambda pemain: pemain["skor"],
        reverse=True
    )

    leaderboard = []
    skor_sebelumnya = None
    peringkat = 0

    for posisi, pemain in enumerate(pemain_urut, start=1):
        if pemain["skor"] != skor_sebelumnya:
            peringkat = posisi

        leaderboard.append({
            "peringkat": peringkat,
            "nama": pemain["nama"],
            "skor": pemain["skor"],
            "level": klasifikasi_level(pemain["skor"])
        })

        skor_sebelumnya = pemain["skor"]

    return leaderboard
