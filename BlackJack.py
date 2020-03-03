import random
import weakref
from pprint import pprint
from operator import attrgetter
previous_value = []


print('Witaj w grze Black Jack ! Postepuj wedlug podpowiedzi i baw sie dobrze, oby los ci sprzyjal !!')
gra = int(input('Podaj ilosc graczy(liczba): '))

# for i in range(gra):

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
        return cls(
            str(input('nazwa_gracza: ')),
            int(input('kwota: ')),
            'karty_gracza')

    # global wrong
    def wrong(self):
        dic_list = list(karty)
        loso = random.choice(dic_list)
        if loso not in previous_value:
            previous_value.append(loso)


    # TUTAJ TRZEBA DOPISAC LOGIKE, ZEBY DLA KOLEJNEGO GRACZA DAWAL KOLEJNE KARTY
    #ta funkcja tutaj powinna
    def losuj_karte(self):
        print (previous_value)
        for i in users.values():
            BlackJack.wrong(self)
            BlackJack.wrong(self)
            i.karty_gracza.extend(previous_value[-2:])
            # print (previous_value)

    #FUNKCJA MA LICZYC WYNIK Z KART. I POKAZYWAC ZWYCIEZCE.. ?
    def licz_wynik(self):
        licz_kar = []
        for i in users.values():
            kar = i.karty_gracza
            print (kar)

            kazdakartawartosc = []
            for kazdakartagracza in kar:
                if kazdakartagracza == 'As_kier' or kazdakartagracza == 'As_karo' or kazdakartagracza == 'As_trefl' or kazdakartagracza == 'As_pik':
                    asy = int(input('Masz Asa! o jaka wartosc chcesz podniesc wynik? 1/10 ?'))
                    if asy == 1:
                        kazdakartawartosc.append(int(1))
                    else:
                        kazdakartawartosc.append(int(10))

                # print
                else:
                    kazdakartawartosc.append(karty[kazdakartagracza])
                print (kazdakartawartosc)
                i.suma.append(sum(kazdakartawartosc))
            print (sum(kazdakartawartosc))

    def wygrany(self):
        for i in users.values():
            su = i.suma
            suli = []
            su2 = max(su)
            suli.append(su2)
            for l in suli:
                print (l)
            print (str('oto maks: ') + str(max(suli)))

            print (str(i.nazwa_gracza) + str(' twoj wynik: ' + str(max(su))))
            

        # print (max(users.values(), key=attrgetter('suma')))
    def druk(self):
        for l in range(gra):
            wybierz_gracza = (input('Wybierz gracza ktoremu dac karte: '))
            drugie_rozdanie = input('kolejna karta ? tak/nie')
            if drugie_rozdanie == 'tak':
                BlackJack.wrong(self)
                print(previous_value)
                for i in BlackJack.insta:
                    if wybierz_gracza == i.nazwa_gracza:
                        print ('tak')
                        #self.karty_gracza.append(previous_value[-1])
                        vars(i)["karty_gracza"].append(previous_value[-1])
                    else:
                        print('nie')

global users
users = {}
for _ in range(gra):
    user = BlackJack.from_input()  # from user input
    users[user.nazwa_gracza] = user


# user.losuj_karte()
# user.licz_wynik()
#print do testow
for i in users.values():
    pprint(vars(i))
#CZY TU MUSI BYC KLASA ?
# class Post_Nowa(BlackJack):
#     def druk(self):
#         for l in range(gra):
#             wybierz_gracza = (input('Wybierz gracza ktoremu dac karte: '))
#             drugie_rozdanie = input('kolejna karta ? tak/nie')
#             if drugie_rozdanie == 'tak':
#                 BlackJack.wrong(self)
#                 print(previous_value)
#                 for i in BlackJack.insta:
#                     if wybierz_gracza == i.nazwa_gracza:
#                         print ('tak')
#                         #self.karty_gracza.append(previous_value[-1])
#                         vars(i)["karty_gracza"].append(previous_value[-1])
#                     else:
#                         print('nie')

user.losuj_karte()
user.licz_wynik()

# Post_Nowa('krupier', 23, []).druk()
user.druk()
user.licz_wynik()
user.wygrany()
