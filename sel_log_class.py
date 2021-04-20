from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs_list import Listy

class Enauczanie:
    def __init__(self, url, button_tag, nr_indeksu, haslo):
        self.url = url
        self.button_tag = button_tag
        self.nr_indeksu = nr_indeksu
        self.haslo = haslo
        self.driver = self.ini_driver()

    def ini_driver(self):
        return webdriver.Chrome()

    def kill_driver(self):
        time.sleep(30)
        self.driver.close()

    def logging(self):
        self.driver.get(self.url)
        przycisk_logowania = self.driver.find_element_by_class_name(self.button_tag)
        przycisk_logowania.click()
        pole_nr_indeksu = self.driver.find_element_by_id("username")
        pole_hasla = self.driver.find_element_by_id("password")
        pole_nr_indeksu.send_keys("s180510")
        pole_hasla.send_keys("KochamAsie123")
        przycisk_logowania_2 = self.driver.find_element_by_class_name(self.button_tag)
        przycisk_logowania_2.click()
        przycisk_logowania_3 = self.driver.find_element_by_class_name(self.button_tag)
        przycisk_logowania_3.click()
        time.sleep(2)

    def get_main_page_html(self):
        return self.driver.page_source

    def get_kursy_html(self):
        obiekt = Listy(self.get_main_page_html())
        lista = obiekt.lista_kursy_linki()
        nazwy_kursow = []
        htmle_kursow = []
        for link in lista:
            self.driver.get(link)
            nazwy_kursow.append(self.driver.title)
            html_tekst = self.driver.page_source
            htmle_kursow.append(html_tekst)
        dict_nazwa_html = {nazwy_kursow[i] : htmle_kursow[i] for i in range(0, len(nazwy_kursow))}
        return dict_nazwa_html