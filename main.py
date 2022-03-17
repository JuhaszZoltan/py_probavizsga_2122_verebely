from datetime import date
from module import elso_feladat 
from module import init_halmaz, get_metszet
from module import init_alklista, get_avg, get_keralk 

print('\n1. feladat:')
elso_feladat()

print('\n2. feladat:')
a = init_halmaz('A')
b = init_halmaz('B')
print(f'\'A\' halmaz elemei: {a}')
print(f'\'B\' halmaz elemei: {b}')
m = get_metszet(a, b)
if (len(m) == 0): print('\'A\'∩\'B\' üres halmaz!')
else: print(f'\'A\'∩\'B\': {m}')

print('\n3. feladat:')
alkalmazottak = init_alklista('employees.txt', 'utf-8')

print(f'3.2: a cégnél {len(alkalmazottak)} programozó dolgozik!')

print(f'3.3: az alkalmazottak havi átlagjövedelme: ${get_avg(alkalmazottak)}')

ker_alkalmazott = get_keralk(input('3.4: írd be a keresett nevet: '), alkalmazottak)
if ker_alkalmazott is None:
    print(f'\tnincs ilyen nevű alkalmazott a cégnél!\n')
else:
    print(f'\téletkor:      {date.today().year - ker_alkalmazott.szul_ev}')
    print(f'\tszékhely:     {ker_alkalmazott.orszag}')
    print(f'\thavi fizetés: {round(ker_alkalmazott.eves_fizetes/12*361.51)} HUF\n')