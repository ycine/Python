import random
import weakref
previous_value = []

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls.nazwa_gracza)


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
        __metaclass__ = IterRegistry
        self.nazwa_gracza = nazwa_gracza
        self.kwota = kwota
        self.karty_gracza = []
        self.instancja = []
        print('Oto nowy gracz: ' + str(self.nazwa_gracza) + str(' kwota wejscia: ' + str(self.kwota)))
        grac.append(self.nazwa_gracza)

        # self.instancja.append(self)
        # self.instancja = self.instancja

    global wrong
    def wrong(self):
        dic_list = list(karty)
        loso = random.choice(dic_list)
        if loso not in previous_value:
                previous_value.append(loso)

    def losuj_karte(self, kolejne_karty, karta1, karta2):
        while len(previous_value) < kolejne_karty:
            wrong(self)
        wylosowane_karty = previous_value[karta1], previous_value[karta2]
        wylosowane_karty_list = list(wylosowane_karty)
        self.karty_gracza.append(wylosowane_karty_list)
        print('karty  gracza: ' + str(self.nazwa_gracza) + str(wylosowane_karty))


    print (previous_value)




gracz1 = BlackJack('theto', 1200, [])
# gracz1.gracz('theto', 1200, [])
gracz1.losuj_karte(2, 0, 1)

gracz2 = BlackJack('erlo', 1600, [])
# gracz2.gracz('erlo', 1600, [])
gracz2.losuj_karte(4, 2, 3)

gracz3 = BlackJack('rter', 2600, [])
# gracz3.gracz('rter', 2600, [])
gracz3.losuj_karte(6, 4, 5)



class Post_Nowa(BlackJack):

    def druk(self):
        ilosc_graczy = len(grac)
        for l in range(ilosc_graczy):
            wybierz_gracza = (raw_input('Wybierz gracza ktoremu dac karte: '))
            drugie_rozdanie = raw_input('kolejna karta ? tak/nie')
            if drugie_rozdanie == 'tak':
                wrong(self)

                for i in BlackJack.insta:

                    if wybierz_gracza == i.nazwa_gracza:
                        print ('tak')
                        #self.karty_gracza.append(previous_value[-1])
                        vars(i)["karty_gracza"].append(previous_value[-1])

                    else:
                        print('nie')

    # def drugie_losowanie(self):
    #
    #
    #     ilosc_graczy = len(grac)
    #     # for i in range(ilosc_graczy):
    #     wybierz_gracza = (raw_input('Wybierz gracza ktoremu dac karte: '))
    #     drugie_rozdanie = raw_input('kolejna karta ? tak/nie')
    #
    #
    #     for insta in BlackJack.nazwa_gracza:
    #         if wybierz_gracza == insta.nazwa_gracza:
    #             print('tak')
    #         else:
    #             print('nie')
    #
    #
    #     # self.instancja.append(self)
    #     # self.instancja = self.instancja
    #     #
    #     # wybierzrz = {}
    #     # wybierzrz[wybierz_gracza] = BlackJack
    #     # print (wybierzrz)
    #
    #     # wybierz_gracza2 = raw_input('Wybierz gracza ktoremu dac karte: ')
    #     # print (wybierzrz[wybierz_gracza2].nazwa_gracza)
    #
    #     #TO POKAZE WSZYSTKIE ATRYBUTY DLA KAZDEGO OBIEKTU
    #     # for attr, value in gracz2.__dict__.iteritems():
    #     #     print(attr, value)
    #     # def wybierz(self):
    #     #     self.karty_gracza.append(wybierz_gracza)
    #
    #
    #     if wybierz_gracza in self.instancja:
    #
    #
    #
    #         print('tak')
    #     else:
    #         print ('nie')
    #
    #     # for i in self.instancja:
    #     #     if hasattr(self.instancja, wybierz_gracza):
    #     #         self.karty_gracza.append(previous_value[-1])
    #         if drugie_rozdanie == 'tak':
    #             wrong(self)
    #             for i in self.instancja:
    #                 print (i)
    #                 # if hasattr(self.instancja, wybierz_gracza):
    #                 #     self.karty_gracza.append(previous_value[-1])
    #                 # self.karty_gracza.append(previous_value[-1])
    #             else:
    #                 pass



# gracz1 = BlackJack('theto', 1200, [])
# # gracz1.gracz('theto', 1200, [])
# gracz1.losuj_karte(2, 0, 1)
#
# gracz2 = BlackJack('erlo', 1600, [])
# # gracz2.gracz('erlo', 1600, [])
# gracz2.losuj_karte(4, 2, 3)
#
# gracz3 = BlackJack('rter', 2600, [])
# # gracz3.gracz('rter', 2600, [])
# gracz3.losuj_karte(6, 4, 5)


# gracz1.drugie_losowanie()
print(previous_value)

post_nowy = Post_Nowa('ttt', 2, []).druk()

from pprint import pprint
pprint(vars(gracz3))
pprint(vars(gracz2))
pprint(vars(gracz1))

print(previous_value)


