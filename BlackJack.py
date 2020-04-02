import random
import weakref
from pprint import pprint

licz_kar = []
listauzytkownikow = []
previous_value = []
dousuniecia = []
print('Witaj w grze Black Jack ! Postepuj wedlug podpowiedzi i baw sie dobrze, oby los ci sprzyjal !!')

while True:
    try:
        gra = int(input('Podaj ilosc graczy(liczba): '))
        break
    except ValueError:
        print('musisz podac liczbe')


class BlackJack():
    global karty
    karty = {'dwojka_pik': 2, 'dwojka_kier': 2, 'dwojka_trefl': 2, 'dwojka_karo': 2,
             'trojka_pik': 3, 'trojka_kier': 3, 'trojka_trefl': 3, 'trojka_karo': 3,
             'czworka_pik': 4, 'czworka_kier': 4, 'czworka_trefl': 4,'czworka_karo': 4,
             'piatka_pik': 5, 'piatka_kier': 5, 'piatka_trefl': 5, 'piatka_karo': 5,
             'szostka_pik': 6, 'szostka_kier': 6, 'szostka_trefl': 6, 'szostka_karo': 6,
             'siodemka_pik': 7, 'siodemka_kier': 7, 'siodemka_trefl': 7,'siodemka_karo': 7,
             'osemka_pik': 8, 'osemka_kier': 8, 'osemka_trefl': 8, 'osemka_karo': 8,
             'dziewiatka_pik': 9, 'dziewiatka_kier': 9, 'dziewiatka_trefl': 9, 'dziewiatka_karo': 9,
             'dziesiatka_pik': 10, 'dziesiatka_kier': 10, 'dziesiatka_trefl': 10, 'dziesiatka_karo': 10,
             'Walet_pik': 10, 'Walet_kier': 10, 'Walet_trefl': 10, 'Walet_karo': 10,
             'Dama_pik': 10, 'Dama_kier': 10, 'Dama_trefl': 10, 'Dama_karo': 10,
             'Krol_pik': 10, 'Krol_kier': 10, 'Krol_trefl': 10, 'Krol_karo': 10,
             'As_pik': [10, 1], 'As_kier': [10, 1], 'As_trefl': [10, 1], 'As_karo': [10, 1]}
    global grac
    grac = []

    insta = []
    def __init__(self, nazwa_gracza, kwota, karty_gracza):
        self.__class__.insta.append(weakref.proxy(self))
        self.nazwa_gracza = nazwa_gracza
        self.kwota = kwota
        self.karty_gracza = []
        self.suma = []
        print('Oto nowy gracz: ' + str(self.nazwa_gracza) + str(' kwota wejscia: ' + str(self.kwota)))
        grac.append(self.nazwa_gracza)


    @classmethod
    def from_input(cls):
        while True:
            grac = str(input('nazwa_gracza: '))
            if grac not in listauzytkownikow:
                listauzytkownikow.append(grac)
                print(listauzytkownikow)
                graj = grac
                break
            else:
                print('uzytkownik z ta nazwa juz istnieje')


        while True:
            try:
                gra = int(input('kwota: '))
                break
            except ValueError:
                print('musisz podac liczbe')
        return cls(
            graj,
            gra,
            'karty_gracza')

    # def __delitem__(self, key):
    #     print('obiekt usuniety')

    def wrong(self):
        dic_list = list(karty)
        loso = random.choice(dic_list)
        if loso not in previous_value:
            previous_value.append(loso)

    # TUTAJ TRZEBA DOPISAC LOGIKE, ZEBY DLA KOLEJNEGO GRACZA DAWAL KOLEJNE KARTY

    def losuj_karte(self):
        # print(previous_value)# tego tez nie potrzeba chyba
        for i in users.values():
            BlackJack.wrong(self)
            BlackJack.wrong(self)
            i.karty_gracza.extend(previous_value[-2:])

    #FUNKCJA MA LICZYC WYNIK Z KART. I POKAZYWAC ZWYCIEZCE.. ?
    def licz_wynik(self):
        print()
        for i in users.values():
            kar = i.karty_gracza
            print(str(i.nazwa_gracza) + ' twoje wylosowane karty: ' + str(kar))

            kazdakartawartosc = []
            for kazdakartagracza in kar:
                if kazdakartagracza not in licz_kar:

                    if kazdakartagracza == 'As_kier' or kazdakartagracza == 'As_karo' or kazdakartagracza == 'As_trefl' or kazdakartagracza == 'As_pik':
                        licz_kar.append(kazdakartagracza)
                        print()
                        asy = int(input('Masz Asa! o jaka wartosc chcesz podniesc wynik? 1/10 ?'))
                        if asy == 1:
                            kazdakartawartosc.append(int(1))
                        else:
                            kazdakartawartosc.append(int(10))
                    else:
                        kazdakartawartosc.append(karty[kazdakartagracza])
                    # print (kazdakartawartosc)
                    i.suma.append(sum(kazdakartawartosc))

                    # print('to ta wartosc.' + str(sum(i.suma[-1:])))
                    if sum(i.suma[-1:]) > 21:
                        # del user

                        print('niestety przegrales, twoj wynik przekroczyl 21')
                    else:
                        pass
                    # print(sum(kazdakartawartosc))

                else:
                    # print(sum(kazdakartawartosc))
                    pass

        for dkey, dvalue in users.items():
            if sum(dvalue.suma[-1:]) > 21:
                dousuniecia.append(dkey)
        for l in dousuniecia:
            if l in list(users.keys()):
                del users[l]

    def wygrany(self):
        print()
        for i in users.values():
            su = i.suma
            suli = []
            su2 = max(su)
            suli.append(su2)
            print(str(i.nazwa_gracza) + str(' twoj wynik: ' + str(max(su))))

    def druk(self):
        for l in range(gra):
            print()
            wybierz_gracza = (input('Wybierz gracza ktoremu dac karte: '))
            drugie_rozdanie = input('kolejna karta ? tak/nie')
            if drugie_rozdanie == 'tak':
                BlackJack.wrong(self)

                for i in BlackJack.insta:
                    if wybierz_gracza == i.nazwa_gracza:
                        # print ('tak')
                        #self.karty_gracza.append(previous_value[-1])
                        vars(i)["karty_gracza"].append(previous_value[-1])
                        print(previous_value[-1:])
                    else:
                        # print('nie')
                        pass

global users
users = {}
for _ in range(gra):
    user = BlackJack.from_input()  # from user input
    users[user.nazwa_gracza] = user

# for i in users.values():
#     pprint(vars(i))


user.losuj_karte()
user.licz_wynik()
user.druk()
user.licz_wynik()
user.wygrany()

# obj = print(max(users.values(), key=attrgetter('suma')))
# for i, v in users.items():
#     print(i, v)

valmax = []
for i in users.values():
    l = (max(i.suma))
    valmax.append(l)
maaks = []
m = max(valmax)
for i in valmax:
    if i == m:
        maaks.append(i)
print()
print('Oto lista zwyciezcow:')
for i in users.values():
    if max(i.suma) == maaks[0]:
        print('Zwyciezca rundy: ' + str(i.nazwa_gracza) + ' z wynikiem: ' + str(max(i.suma)))
    else:
        i = None

#kolejne losowanie

