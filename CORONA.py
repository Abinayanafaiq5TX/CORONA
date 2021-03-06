U
    Ιν^:W  γ                   @   sx  d dl Z d dlZd dlZd dlZd dlZd dlmZmZ d dlmZ e d‘ e 	‘  dd Z
dd Zd	d
 Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd  Zd!d" Zd#d$ Zd%d& Zd'd( Zd)d* Zd+d, Zd-d. Zd/d0 Zd1d2 Z d3d4 Z!d5d6 Z"d7d8 Z#d9d: Z$d;d< Z%d=d> Z&d?d@ Z'dAdB Z(dCdD Z)dEdF Z*dGdH Z+dIdJ Z,e+  dS )Kι    N)ΪlogoΪABIN)ΪForeΪclearc                  C   s    t  d‘j} t| }t d|‘}ttd}t dt|‘}t| dd‘ dd‘ d	d
‘}t| dd‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nϊ/https://api.kawalcorona.com/indonesia/provinsi/ϊ{"attributes":{.*?}zMASUKAN NAMA PROVINSIzO"Provinsi":"DKI Jakarta","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?Ϊ
Kasus_Posiϊ
POSITIF = Ϊ
Kasus_Sembϊ	SEMBUH = Ϊ
Kasus_MeniϊMENINGGAL = ϊ]Ϊ ϊ'ϊ[ϊ}ϊ,ϊ"ϊ )	ΪrequestsΪgetΪtextΪstrΪreΪfindallΪinputΪreplaceΪprint)ΪabinΪabin1Ϊabin2Zabin6Ϊabin3Ϊabin4Ϊabin5© r%   ϊREGEX.pyΪjakarta   s     8r'   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zN"Provinsi":"Jawa Timur","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   ©r   r   r   r   r   r   r   r   ©r   r    r!   r"   r#   r$   r%   r%   r&   Ϊ
Jawa_Timur   s     8r*   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zT"Provinsi":"Sulawesi Selatan","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSulawesi_Selatan   s     8r+   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zN"Provinsi":"Jawa Barat","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   Ϊ
Jawa_Barat!   s     8r,   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zI"Provinsi":"Papua","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪPapua)   s     8r-   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zV"Provinsi":"Kalimantan Selatan","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKalimantan_Selatan1   s     8r.   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zT"Provinsi":"Sumatera Selatan","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSumatera_Selatan9   s     8r/   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zJ"Provinsi":"Banten","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪBantenA   s     8r0   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zW"Provinsi":"Nusa Tenggara Barat","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪNusa_Tenggara_BaratI   s     8r1   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zR"Provinsi":"Sumatera Utara","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSumatera_UtaraQ   s     8r2   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zH"Provinsi":"Bali","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪBaliY   s     8r3   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zR"Provinsi":"Sumatera Barat","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSumatera_Barata   s     8r4   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zR"Provinsi":"Sulawesi Utara","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSulawesi_Utarai   s     8r5   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zU"Provinsi":"Kalimantan Tengah","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKalimantan_Tengahq   s     8r6   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zJ"Provinsi":"Maluku","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪMalukuy   s     8r7   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zT"Provinsi":"Kalimantan Timur","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKalimantan_Timur   s     8r8   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zP"Provinsi":"Maluku Utara","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪMaluku_Utara   s     8r9   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zU"Provinsi":"Sulawesi Tenggara","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSulawesi_Tenggara   s     8r:   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zT"Provinsi":"Kalimantan Barat","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKalimantan_Barat   s     8r;   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   z^"Provinsi":"Daerah Istimewa Yogyakarta","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪDaerah_Istimewa_Yogyakarta‘   s     8r<   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zR"Provinsi":"Kepulauan Riau","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKepualauan_Riau©   s     8r=   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zO"Provinsi":"Papua_Barat","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪPapua_Barat±   s     8r>   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zM"Provinsi":"Gorontalo","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   Ϊ	GorontaloΉ   s     8r?   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zT"Provinsi":"Kalimantan Utara","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKalimantan_UtaraΑ   s     8r@   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zS"Provinsi":"Sulawesi Tengah","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSulawesi_TengahΙ   s     8rA   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zK"Provinsi":"Lampung","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪLampungΡ   s     8rB   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zT"Provinsi":"Kepulauan Bangka","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪKepulauan_BangkaΩ   s     8rC   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zH"Provinsi":"Riau","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪRiauα   s     8rD   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zI"Provinsi":"Jambi","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪJambiι   s     8rE   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zW"Provinsi":"Nusa_Tenggara_Timur","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪNusa_Tenggara_Timurρ   s     8rF   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zL"Provinsi":"Bengkulu","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪBengkuluω   s     8rG   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zR"Provinsi":"Sulawesi Barat","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪSulawesi_Barat  s     8rH   c                  C   s   t  d‘j} t| }t d|‘}t dt|‘}t| dd‘ dd‘ dd	‘}t| d
d‘ dd‘ dd‘ dd‘ dd‘ dd‘}t| d S )Nr   r   zH"Provinsi":"Aceh","Kasus_Posi":.*?,"Kasus_Semb":.*?,"Kasus_Meni":.....*?r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r(   r)   r%   r%   r&   ΪAceh	  s     8rI   c                  C   s$  t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d	 t tj dtj d
tj d ttj dtj dtj d} | dkrΤt d‘ nL| dkrθt d‘ n8| dkrόt d‘ n$| dkrt ‘  n| d
kr t	  d S )Nr   Ϊ1z].HUB AUTHORΪ2z].SUBSCRIBE CHANNEL AUTHORΪ3z].UPDATE SCRIPTΪ4z#].LIHAT TOTAL DATA CORONA INDONESIAΪ5z].LIHAT DATA CORONA PROVINSIϊ!z].PILIH:z%xdg-open https://wa.me/+6285600928643z%xdg-open https://youtu.be/9X-qHEodKDwzgit pull)
r   r   ΪWHITEΪMAGENTAr   ΪosΪsystemr   ZcoronaΪnaya)Zabinzr%   r%   r&   Ϊmenu  s           


rU   c                  C   s   t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d	 t tj dtj d
tj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj dtj d t tj dtj d tj d! t tj dtj d"tj d# t tj dtj d$tj d% t tj dtj d&tj d' t tj dtj d(tj d) t tj dtj d*tj d+ t tj dtj d,tj d- t tj dtj d.tj d/ t tj dtj d0tj d1 t tj dtj d2tj d3 t tj dtj d4tj d5 t tj dtj d6tj d7 t tj dtj d8tj d9 t tj dtj d:tj d; t tj dtj d<tj d= t tj dtj d>tj d? t tj dtj d@tj dA t tj dtj dBtj dC tdD} | dkr<t  n`| dkrPt  nL| dkrdt  n8| dkrxt  n$| d
krt	  n| dkr t
  nό| dkr΄t  nθ| dkrΘt  nΤ| dkrάt  nΐ| dkrπt  n¬| dkrt  n| dkrt  n| dkr,t  np| dkr@t  n\| dkrTt  nH| d krht  n4| d"kr|t  n | d$krt  n| d&kr’t  nϊ| d(kr΄t  nθ| d*krΖt  nΦ| d,krΨt  nΔ| d.krκt  n²| d0krόt  n | d2krt  n| d4kr t  n|| d6kr2t  nj| d8krDt   nX| d:krVt!  nF| d<krht"  n4| d>krzt#  n"| d@krt$  n| dBkrt%  d S )ENr   rJ   z]JAKARTArK   z]JAWA TIMURrL   z]Sulawesi SelatanrM   z]Jawa BaratrN   z]PapuaΪ6z]Kalimantan SelatanΪ7z]Sumatera SelatanΪ8z]BantenΪ9z]Nusa Tenggara BaratZ10z]Sumatera UtaraZ11z]BaliZ12z]Sumatera BaratZ13z]Sulawesi UtaraZ14z]Kalimantan TengahZ15z]MalukuZ16z]Kalimantan TimurZ17z]Maluku UtaraZ18z]Sulawesi TenggaraZ19z]Kalimantan BaratZ20z]Daerah Istimewa YogyakartaZ21z]Kepulauan RiauZ22z]Papua BaratZ23z
]GorontaloZ24z]Kalimantan UtaraZ25z]Sulawesi TengahZ26z]LampungZ27z]Kepulauan BangkaZ28z]RiauZ29z]JambiZ30z]Nusa Tenggara TimurZ31z	]BengkuluZ32z]Sulawesi BaratZ33z]AcehzPILIH:)&r   r   rP   rQ   r   r'   r*   r+   r,   r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r<   ZKepulauan_Riaur>   r?   r@   rA   rB   rC   rD   rE   rF   rG   rH   rI   )Zhambuhr%   r%   r&   rT   "  sΘ                                     


















































rT   )-r   r   rR   ZcoloramaZabinkunsr   r   r   rS   Zbannerr'   r*   r+   r,   r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r<   r=   r>   r?   r@   rA   rB   rC   rD   rE   rF   rG   rH   rI   rU   rT   r%   r%   r%   r&   Ϊ<module>   sR   
	k