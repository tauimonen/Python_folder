class Auto:
    def __init__(self, kulutus):
        self.kulutus = kulutus


class Mittari:

    def laske_kulutus(self, auto, matka, nopeus):
        bensan_kulutus = float(auto.kulutus)
        for i in range(int(nopeus)):
            bensan_kulutus *= 1.009
        kok_kulutus = bensan_kulutus * float(matka) / 100
        return kok_kulutus

    def kayttoliittyma(self):
        tyyppi = input("Anna autotyyppi: ")
        matka = input("Anna matka: ")
        nopeus1 = input("Anna ensimmäinen nopeus: ")
        nopeus2 = input("Anna toinen nopeus: ")

        if tyyppi == "a":
            autotyyppi = Auto(3)
        if tyyppi == "b":
            autotyyppi = Auto(3.5)
        if tyyppi == "c":
            autotyyppi = Auto(4)

        kulutus1 = self.laske_kulutus(autotyyppi, matka, nopeus1)
        kulutus2 = self.laske_kulutus(autotyyppi, matka, nopeus2)

        print(50*"=")
        print(f"Kulutus tyypillä {tyyppi}, matkalla: {matka} ja nopeudella: {nopeus1} on {kulutus1} litraa.")
        print(f"Kulutus tyypillä {tyyppi}, matkalla: {matka} ja nopeudella: {nopeus2} on {kulutus2} litraa.")


if __name__ == "__main__":
    mittari = Mittari()
    mittari.kayttoliittyma()


