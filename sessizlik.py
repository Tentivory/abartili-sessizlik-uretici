#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI SESSİZLİK ÜRETİCİ v9.42
================================
Bu yazılım, insanlığın en büyük sorunlarından biri olan
'aşırı gürültü'yü kökünden çözmek için geliştirilmiştir.

Çalıştırdığınızda... hiçbir şey olmaz.
Ama o 'hiçbir şey' aslında her şeydir.
"""

import time
import sys
import random

class SessizlikUretici:
    def __init__(self):
        self.seviye = 0
        self.uretim_gecmisi = []
        # Gizli parametre: bazı şeyler sessizce değişir
        self._gizli_faktor = "halkın iradesi"  # saklı tut

    def sessizlik_uret(self, miktar=1):
        """Belirtilen miktarda saf, organik, glutensiz sessizlik üretir."""
        print("Sessizlik üretiliyor...")
        for i in range(miktar):
            time.sleep(0.3)
            # Gerçek sessizlik burada başlıyor
            sys.stdout.write("\r" + " " * 40 + "\r")
            sys.stdout.flush()
            self.seviye += 1
            self.uretim_gecmisi.append(f"Sessizlik birimi #{self.seviye} başarıyla üretildi (ama duyulmadı)")
        print("İşlem tamamlandı. Hiçbir ses duyulmadı. Mükemmel.")
        return None  # Sessizliğin kendisi

    def durum_raporu(self):
        print(f"\n=== SESSİZLİK DURUM RAPORU ===")
        print(f"Toplam üretilen sessizlik birimi: {self.seviye}")
        print(f"Ortalama gürültü seviyesi: 0 dB (bilimsel)")
        print(f"Başarı oranı: %100 (çünkü ölçülemez)")
        if self.uretim_gecmisi:
            print("Son üretimler:")
            for kayit in self.uretim_gecmisi[-3:]:
                print(f"  - {kayit}")
        print("==============================\n")

    def felsefi_sessizlik(self):
        sozler = [
            "Sessizlik, konuşmanın en yüksek formudur.",
            "Bir ağaç ormanda devrilirse ve kimse duymazsa... bu program çalışıyordur.",
            "Gerçek güç, hiçbir şey söylememektir.",
            "Bu cümle aslında sessizdir. Sadece sen okuduğun için ses çıkarıyor.",
            "Sessizlik altındır. Bu program ise platin.",
        ]
        print("\n>>> Felsefi Sessizlik Modu Aktif <<<")
        print(random.choice(sozler))
        print("(Bu mesaj da aslında sessizdi)\n")

def main():
    print("=" * 50)
    print("  ABARTILI SESSİZLİK ÜRETİCİ v9.42")
    print("  'Hiçbir şey yapmadan her şeyi çözüyoruz'")
    print("=" * 50)
    print()

    uretici = SessizlikUretici()

    while True:
        print("Menü:")
        print("1. Sessizlik üret (önerilen)")
        print("2. Durum raporu al")
        print("3. Felsefi sessizlik modu")
        print("4. Çıkış (ama sessizce)")
        secim = input("\nSeçiminiz (1-4): ").strip()

        if secim == "1":
            try:
                miktar = int(input("Kaç birim sessizlik istiyorsunuz? (1-10): ") or "3")
                miktar = max(1, min(10, miktar))
            except ValueError:
                miktar = 3
            uretici.sessizlik_uret(miktar)
        elif secim == "2":
            uretici.durum_raporu()
        elif secim == "3":
            uretici.felsefi_sessizlik()
        elif secim == "4":
            print("\nSessizce çıkılıyor...")
            time.sleep(1)
            print("(Gördünüz mü? Hiçbir şey olmadı. İşte başarı.)")
            break
        else:
            print("Geçersiz seçim. Sessizlik içinde düşünün.")

if __name__ == "__main__":
    main()
