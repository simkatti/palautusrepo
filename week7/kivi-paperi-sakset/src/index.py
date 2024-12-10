from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def main():
    print("Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
            )

    vastaus = input()
    print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

    if vastaus.endswith("a"):
        pelimoodi = 'a'
    elif vastaus.endswith("b"):
        pelimoodi = 'b'     
    elif vastaus.endswith("c"):
        pelimoodi = 'c'

    peli = luo_peli(pelimoodi)
    peli.pelaa()


def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()

    return None


if __name__ == "__main__":
    main()
