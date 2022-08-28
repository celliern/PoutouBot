import random
import importlib.resources as pkg_resources
from . import resources

list_manger = pkg_resources.read_text(resources, "list_manger.txt").split("\n")
list_main = pkg_resources.read_text(resources, "list_main.txt").split("\n")

def jai_faim():
    return f"{random.choice(list_manger)} {random.choice(list_main)}"

if __name__=="__main__":
    print(jai_faim())