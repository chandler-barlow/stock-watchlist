import load_config
import poll_market
import sys
import os
import time
from colorama import Fore, Back, Style
conf = load_config.start()
run = True
while run:
    os.system("clear")
    watchlist = poll_market.poll(conf["watchlist"])
    print(Back.WHITE + Fore.BLACK + "Fetching watchlist data.")
    if conf["options"]["delay"] > 0:
        print(Back.WHITE + Fore.BLACK + "Delay set at", conf["options"]["delay"], "minutes.")
    print(Style.RESET_ALL, end="")
    for company in watchlist:
        wc = company.info
        if wc["open"] > wc["bid"]:
            print(Fore.RED + "[ DOWN ] ", end=" ")
        else:
            print(Fore.GREEN + "[  UP  ] ", end=" ")
        print(Style.RESET_ALL,end="")
        print( "Symbol:" ,  wc["symbol"] , "- Name:", wc["shortName"], "- Price:", wc["bid"], "- Open:", wc["open"])
    if conf["options"]["delay"] == 0:
        run = False
    else:
        time.sleep(conf["options"]["delay"] * 60)
