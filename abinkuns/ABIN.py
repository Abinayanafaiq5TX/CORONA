import os, requests, sys, json
import re
import colorama 
from abinkuns import logo
from colorama import Fore
from colorama import Style

Sembuh = 0
Meninggal = 0
Konfirmasi = 0

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'


def corona():
	os.system('clear')
	logo.banner()
	b = requests.get('https://api.kawalcorona.com/indonesia').text
	z = re.findall(r'"dirawat":"(.*?)"', b)
	a = re.findall(r'"meninggal":"(.*?)"', b)
	po = re.findall(r'"positif":"(.*?)"', b)
	q = re.findall(r'"sembuh":"(.*?)"', b)

	dir = str(z)
	men = str(a)
	pos = str(po)
	sem = str(q)
	#positif = po.replace("'","").replcae("]","").replace("[","")
	positif = str(po).replace("'","").replace("]","").replace("[","")
	meninggal = men.replace("'","").replace("]","").replace("[","")
	sembuh = sem.replace("'","").replace("]","").replace("[","")
	dirawat = dir.replace("'","").replace("]","").replace("[","")
	print(f'{Fore.WHITE}[{Fore.YELLOW}•{Fore.WHITE}]{Fore.RED}DIRAWAT{Fore.GREEN} {Fore.MAGENTA}= {Fore.WHITE}[{dirawat}]')
	#print(f'{Fore.WHITE}=' * 50)
	print(f'{Fore.WHITE}[{Fore.YELLOW}•{Fore.WHITE}]{Fore.YELLOW}POSITIF{Fore.GREEN} {Fore.MAGENTA}= {Fore.WHITE}[{positif}]')
	#print(f'{Fore.WHITE}=' * 50)
	print(f'{Fore.WHITE}[{Fore.YELLOW}•{Fore.WHITE}]{Fore.CYAN}MENINGGAL{Fore.GREEN} {Fore.MAGENTA}= {Fore.WHITE}[{meninggal}]')
	#print(f'{Fore.WHITE}=' * 50)
	print(f'{Fore.WHITE}[{Fore.YELLOW}•{Fore.WHITE}]{Fore.BLUE}SEMBUH{Fore.GREEN} {Fore.MAGENTA}= {Fore.WHITE}[{sembuh}]')
