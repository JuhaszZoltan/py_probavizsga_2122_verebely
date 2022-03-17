def elso_feladat() -> None:
    n:int = int(input('Írj be egy egész számot: '))
    s:str = input('Írj be egy tetszőleges szöveget: ').upper() + ' '
    print(f'megoldás: {n * s}')


def init_halmaz(betujel:str) -> list[int]:
    halmaz:list[int] = []
    while True:
        e = input(f'\'{betujel}\' halmaz {len(halmaz) + 1}. eleme: ')
        if len(e) == 0:
            print(f'\'{betujel}\' halmaz feltöltése befejeződött!')
            return halmaz
        if int(e) in halmaz:
            print(f'HIBA! a(z) {e} már benne van a(z) \'{betujel}\' halmazban!')
        else: halmaz.append(int(e))


def get_metszet(a_halmaz:list[int], b_halmaz:list[int]) -> list[int]:
    metszet_halmaz:list[int] = []
    for e in a_halmaz:
        if e in b_halmaz:
            metszet_halmaz.append(e)
    return metszet_halmaz


class Alkalmazott:
    def __init__(self, sor:str):
        spl:list[str] = sor.strip().split(';')
        self.nev:str = spl[0]
        self.eves_fizetes:int = int(spl[1].strip('$'))
        self.szul_ev:int = int(spl[2])
        self.orszag:str = spl[3]


def init_alklista(file:str, encoding:str) -> list[Alkalmazott]:
    alklista:list[Alkalmazott] = []
    for sor in open(file=file, encoding=encoding):
        alklista.append(Alkalmazott(sor))
    return alklista


def get_avg(alklista:list[Alkalmazott]) -> float:
    sum = 0
    for a in alklista:
        sum += a.eves_fizetes
    return round(sum/len(alklista)/12, 2)


def get_keralk(ker_nev:str, alklista:list[Alkalmazott]) -> Alkalmazott:
    for a in alklista:
        if a.nev.lower() == ker_nev.lower():
            return a
    return None
