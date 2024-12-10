from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmainen_siirto=None):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto