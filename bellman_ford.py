class Verkko:
    def __init__(self, solmut):
        self.solmut = solmut
        self.verkko = []

    def lisaa_kaari(self, u, v, w):
        self.verkko.append([u, v, w])

    def tulosta(self, etaisyys):
        print("Etäisyys")
        for i in range(self.solmut):
            print("{0}\t\t{1}".format(i, etaisyys[i]))

    def bf(self, lahto):
        etaisyys = [float("Inf")] * self.solmut
        etaisyys[lahto] = 0

        for _ in range(self.solmut -1):
            for u, v, w, in self.verkko:
                if etaisyys[u] != float("Inf") and etaisyys[u] + w < etaisyys[v]:
                    etaisyys[v] = etaisyys[u] + w
        for u, v, w in self.verkko:
            if etaisyys[u] != float("Inf") and etaisyys[u] + w <etaisyys[v]:
                print("negatiivinen sykli")
                return
        self.tulosta(etaisyys)


verkko = Verkko(5)
verkko.lisaa_kaari(0, 1, -1)
verkko.lisaa_kaari(0, 2, 4)
verkko.lisaa_kaari(1, 2, 3)
verkko.lisaa_kaari(1, 3, 2)
verkko.lisaa_kaari(1, 4, 2)
verkko.lisaa_kaari(3, 2, 5)
verkko.lisaa_kaari(3, 1, 1)
verkko.lisaa_kaari(4, 3, -3)


verkko.bf(0)
