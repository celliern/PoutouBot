import requests
from bs4 import BeautifulSoup


def bientot_le_weekend():
    url = "https://estcequecestbientotleweekend.fr/"
    resp = requests.get(url)
    return (
        BeautifulSoup(resp.content, "html.parser").find("p", class_="msg").text.strip()
    )


def bientot_l_apero():
    url = "https://estcequecestbientotlapero.fr/"
    resp = requests.get(url)
    return (
        BeautifulSoup(resp.content, "html.parser").find("h2").find("font").text.strip()
    )
