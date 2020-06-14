import os, sys, time, colorama
from colorama import Fore
w = '\x1b[1;37m'
b = '\x1b[1;36m'
g = '\x1b[1;32m'
y = '\x1b[1;33m'
r = '\x1b[1;31m'
def ketik(s):
	for x in s +'\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(2.0/90)



def banner():
	ketik(f'''

{Fore.WHITE}╔═╗╔═╗╦═╗╔═╗╔╗╔╔═╗
{Fore.WHITE}║  ║ ║╠╦╝║ ║║║║╠═╣
{Fore.RED}╚═╝╚═╝╩╚═╚═╝╝╚╝╩ ╩
{w}╔═════════════════════════════════════════╗
{w}║{y}*{w} Author{r} :{b} ABIN XD.5TX                {w}   ║
{w}║{y}*{w} Forum {r} :{b} OFC Cyber Zet {w}|{b}D4RK5.5TX{w}      ║
{w}║{y}*{w} YOUTUBE{r} :{g} \x1b[4mBENJAMIN ID\x1b[0m{w}                  ║
{w}╚═════════════════════════════════════════╝ ''')