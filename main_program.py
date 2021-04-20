from sel_log_class import Enauczanie
from bs_list import Listy
import json

url = "https://enauczanie.pg.edu.pl/moodle/login/"
przycisk = "btn-submit"
with open("test.txt") as f:
    lines = f.readlines()
loger = Enauczanie(url, przycisk, lines[0], lines[1])
loger.ini_driver()
loger.logging()

dict_nazwa_html = loger.get_kursy_html()
dict_nazwa_linki = Listy.dict_nazwa_linki_list(dict_nazwa_html)

print(json.dumps(dict_nazwa_linki, indent=3))
loger.kill_driver()