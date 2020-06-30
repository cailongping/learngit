from random import randint
from time import sleep
import colorama
from colorama import Fore,Back,Style

colorama.init()
rnd2=randint(1,60)

def gentree():
    for x in range(1,30,2):
        rnd1=randint(1,rnd2)
        if x==1:
            ch="$"
        elif rnd1 % 4==0:
            ch="o"
        elif rnd1 % 3==0:
            ch="j"
        elif rnd1 % 5==0:
            ch="o"
        elif rnd1 % 7==0:
            ch="j"
        else:
            ch="*"

        if ch=="$":
            print(Fore.RED+"{:^33}".format(ch*x))
        elif ch=="o":
            print(Fore.RED + "{:^33}".format(ch * x))
        elif ch=="j":
            print(Fore.YELLOW + "{:^33}".format(ch * x))
        else:
            print(Fore.GREEN + "{:^33}".format(ch * x))
    print("{:^33}".format('|||'))
    print("{:^33}".format('|||'))
    print("{:^33}".format('Merry_christmas'))
    sleep(.24)

gentree()

