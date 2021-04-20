from bs4 import BeautifulSoup

class Listy:
    def __init__(self, main_html):
        self.main_html = main_html

    def lista_kursy_linki(self):
        lista = []
        soup = BeautifulSoup(self.main_html, "html.parser")
        for div in soup.find_all("div", {"class":"card dashboard-card lookup-card"}):
            for link in div.select("a"):
                if(link['href']!= '#'):
                    lista.append(link['href'])
        lista = list(dict.fromkeys(lista))
        return lista

    @staticmethod
    def link_kryterium(dict_nazwa_linki, kryterium):
        pass

    @staticmethod
    def dict_nazwa_linki_list(dict_nazwa_html):   #list(newdict.keys()) dla nazw kursów z dict_nazwa_html
        nazwy_kursow = list(dict_nazwa_html.keys())
        dict_nazwa_linki = {nazwy_kursow[i] : [] for i in range(0, len(nazwy_kursow))}
        for key in dict_nazwa_html:
            soup = BeautifulSoup(dict_nazwa_html[key], "html.parser")
            for div in soup.find_all("div", {"class":"activityinstance"}):
                for link in div.select("a.aalink"):
                    dict_nazwa_linki[key].append(link['href'])
            dict_nazwa_linki[key].sort()

        return dict_nazwa_linki
    