import random

previous_value = []
class BlackJack():


    def gracz(self, nazwa_gracza, kwota):
        self.nazwa_gracza = nazwa_gracza
        self.kwota = kwota
        print str('Oto nowy gracz: ' + str(self.nazwa_gracza) + str(' kwota wejscia: ' + str(self.kwota)))


    def losowanie(self):
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

    global wrong
    def wrong(self):
        dic = {'perwsza': 1, 'druga': 2, 'trzecia': 3, 'czwarta': 4, 'piata': 5, 'szosta': 6}
        dic_list = list(dic)
        loso = random.choice(dic_list)
        if loso not in previous_value:
                previous_value.append(loso)

    def losuj_karte(self, kolejne_karty, nazwa_gracza, karta1, karta2):

        while len(previous_value) < kolejne_karty:
            wrong(self)
        wylosowane_karty = previous_value[karta1], previous_value[karta2]

        print str('karty  gracza ' + str(self.nazwa_gracza) + str(wylosowane_karty))


    print previous_value
    # losuj_karte(2, 'mario', 0, 1)
    #
    #
    # losuj_karte(4, 'theto', 2, 3)
    #
    #
    # losuj_karte(6, 'erne', 4, 5)


#TUTAJ JEST POTRZEBNE PRORAMOWANIE OBIEKTOWE ZEBY DLA KAZDEGO GRACZA PRZYPISYWAC WARTOSCI



gracz1 = BlackJack()
gracz1.gracz('theto', 1200)
gracz1.losuj_karte(2, 'er', 0, 1)


gracz2 = BlackJack()
gracz2.gracz('erlo', 1600)
gracz2.losuj_karte(4, 'er', 2, 3)

gracz3 = BlackJack()
gracz3.gracz('rter', 2600)
gracz3.losuj_karte(6, 'er', 4, 5)