# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 00:15:14 2018

@author: LordNassel
"""
#%%
"""
Feladat: 
    
Eszemiszom (az eszem izom :D ) városában időközi helyhatósági választásokat írtak ki. A városban összesen
12 345 szavazásra jogosult állampolgár van, akiket nyolc választókerületbe soroltak.
Minden választókerületben több jelölt is indul, de egy jelölt csak egy választókerületben
indulhat. Egy választókerület szavazói az adott választókerületben induló jelöltek közül egy
jelöltre adhatnak le szavazatot, de nem kötelező részt venniük a szavazáson. Minden
választókerületben az a jelölt nyer, aki a legtöbb szavazatot kapja. (Feltételezheti, hogy
egyetlen választókerületben sem alakult ki holtverseny.)
A jelöltek vagy egy párt támogatásával, vagy független jelöltként indulhatnak. Az idei
évben a Gyümölcsevők Pártja (GYEP), a Húsevők Pártja (HEP), a Tejivók Szövetsége (TISZ)
vagy a Zöldségevők Pártja (ZEP) támogatja a jelölteket.
A szavazás eredményét a szavazatok.txt szóközökkel tagolt fájl tartalmazza,
amelynek minden sorában egy-egy képviselőjelölt adatai láthatók.

Például:
8 149 Zeller Zelma ZEP
6 63 Zsoldos Zsolt -

Az első két adat a választókerület sorszáma és a képviselőjelöltre leadott szavazatok
száma. Ezt a jelölt vezeték- és utóneve, majd a jelöltet támogató párt hivatalos rövidítése
követi. Független jelöltek esetében a párt rövidítése helyett egy kötőjel szerepel. Minden
képviselőjelöltnek pontosan egy utóneve van.
Készítsen programot valasztas néven, amely az alábbi kérdésekre válaszol!
Minden részfeladat feldolgozása során írja ki a képernyőre a részfeladat sorszámát,
(például: 2. feladat)! Ahol a felhasználótól kér be adatot,ott írja ki a képernyőre azt is,
hogy milyen adatot vár! Az ékezetmentes kiírás is elfogadott.
"""
#%%
"""
1. Olvassa be a szavazatok.txt fájl adatait, majd ezek felhasználásával oldja meg
a következő feladatokat! Az adatfájlban legfeljebb 100 képviselőjelölt adatai szerepelnek.
"""
import sys
 
with open("szavazatok.txt", "r") as filepointer:
    array = []
    for line in filepointer:
        info = line.replace('\n','').split(' ')
        array.append(info)
    filepointer.close()
print(array)
print(array[0][0])
print(array[0][1])
print(array[0][2])
print(array[0][3])
print(array[0][4])
print(len(array))


#%%
"""
2. Hány képviselőjelölt indult a helyhatósági választáson? A kérdésre egész mondatban
válaszoljon az alábbi mintához hasonlóan:
A helyhatósági választáson 92 képviselőjelölt indult.
"""
print("A helyhatósági választáson %d képviselőjelölt indult." % len(array))

#%%
"""
3. Kérje be egy képviselőjelölt vezetéknevét és utónevét, majd írja ki a képernyőre, hogy
az illető hány szavazatot kapott! Ha a beolvasott név nem szerepel a nyilvántartásban, úgy
jelenjen meg a képernyőn az „Ilyen nevű képviselőjelölt nem szerepel
a nyilvántartásban!” figyelmeztetés! A feladat megoldása során feltételezheti, hogy
nem indult két azonos nevű képviselőjelölt a választáson.
"""
vezeteknev = input("Vezeteknev: ")
keresztnev = input("Keresztnev: ")
checkpoint = 0
for i in range(0,len(array)):
    if((array[i][2] == vezeteknev and (array[i][3] == keresztnev))):
        szavazatszam = int(array[i][1])
        print("%s %s %d db szavazatot kapott!"% (vezeteknev, keresztnev, szavazatszam))
        checkpoint = 1
if(checkpoint == 0):
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")


#%%
"""
4. Határozza meg, hányan adták le szavazatukat, és mennyi volt a részvételi arány!
(A részvételi arány azt adja meg, hogy a jogosultak hány százaléka vett részt
a szavazáson.) A részvételi arányt két tizedesjegy pontossággal, százalékos formában írja
ki a képernyőre!
Például:
A választáson 5001 állampolgár, a jogosultak 40,51%-a vett részt.
"""
leadott_szavazat=0
allampolgar=12345

for i in range(0,len(array)):
    szam = int(array[i][1])
    leadott_szavazat = leadott_szavazat + szam
    
reszveteli_arany=((leadott_szavazat)/(allampolgar))
szazalek = reszveteli_arany*100

print("A valasztason %d allampolgar, a jogosultak %f szazaleka vett reszt" % (leadott_szavazat,szazalek))


#%%
"""
5. Határozza meg és írassa ki a képernyőre az egyes pártokra leadott szavazatok arányát
az összes leadott szavazathoz képest két tizedesjegy pontossággal! A független jelölteket
együtt, „Független jelöltek” néven szerepeltesse!
Például:
Zöldségevők Pártja= 12,34%
Független jelöltek= 23,40%
"""
gyumolcsevok = 0
husevok = 0
tejivok = 0
zoldsegevok = 0
fuggetlenek = 0

for i in range(0,len(array)):
    if((array[i][4] == 'GYEP')):
        gyumolcsevok = gyumolcsevok + int(array[i][1])
    if((array[i][4] == 'HEP')):
        husevok = husevok + int(array[i][1])
    if((array[i][4] == 'TISZ')):
        tejivok = tejivok + int(array[i][1])
    if((array[i][4] == 'ZEP')):
        zoldsegevok = zoldsegevok + int(array[i][1])
    if((array[i][4] == '-')):
        fuggetlenek = fuggetlenek + int(array[i][1])
        
sz_gyumolcsevok = ((gyumolcsevok)/(leadott_szavazat))*100
sz_husevok = ((husevok)/(leadott_szavazat))*100
sz_tejivok = ((tejivok)/(leadott_szavazat))*100
sz_zoldsegevok = ((zoldsegevok)/(leadott_szavazat))*100
sz_fuggetlenek = ((fuggetlenek)/(leadott_szavazat))*100 

print("Zöldségevők pártja: %f\n Függetlenek: %f \n Husevok: %f\n Tejivók: %f \n Gyümölcsevők: %f\n"%(sz_zoldsegevok,sz_fuggetlenek,sz_husevok,sz_tejivok,sz_gyumolcsevok))   


#%%
"""
6. Melyik jelölt kapta a legtöbb szavazatot? Jelenítse meg a képernyőn a képviselő vezetékés
utónevét, valamint az őt támogató párt rövidítését, vagy azt, hogy független! Ha több
ilyen képviselő is van, akkor mindegyik adatai jelenjenek meg!
"""
maxszavazat = 0

for i in range(0,len(array)):
    szam=int(array[i][1])
    if((maxszavazat) < (szam)):
        maxszavazat = szam
for i in range(0,len(array)):
    szam=int(array[i][1])
    if(maxszavazat == szam):
        vezeteknev=array[i][2]
        keresztnev=array[i][3]
        part=array[i][4]
        if((part) == ("-")):
            part = "független"
        print("%s %s kapta a legtöbb szavazatot ami %d darab - %s " % (vezeteknev,keresztnev,maxszavazat,part))


#%%
"""
7. Határozza meg, hogy az egyes választókerületekben kik lettek a képviselők! Írja ki
a választókerület sorszámát, a győztes vezeték- és utónevét, valamint az őt támogató párt
rövidítését, vagy azt, hogy független egy-egy szóközzel elválasztva
a kepviselok.txt nevű szöveges fájlba! Az adatok a választókerületek száma szerinti
sorrendben jelenjenek meg! Minden sorba egy képviselő adatai kerüljenek!
"""
##Nyolc választókerület van

egy = 0
ketto = 0
harom = 0
negy = 0
ot = 0
hat = 0
het = 0
nyolc = 0
szavazat = 0

for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    if(kerulet == 1):
        if(szavazat > egy):
            egy = szavazat
        
    if(kerulet == 2):
        if(szavazat > ketto):
            ketto = szavazat
            
    if(kerulet == 3):
        if(szavazat > harom):
            harom = szavazat
            
    if(kerulet == 4):
        if(szavazat > negy):
            negy = szavazat
            
    if(kerulet == 5):
        if(szavazat > ot):
            ot = szavazat
            
    if(kerulet == 6):
        if(szavazat > hat):
            hat = szavazat
            
    if(kerulet == 7):
        if(szavazat > het):
            het = szavazat
            
    if(kerulet == 8):
        if(szavazat > nyolc):
            nyolc = szavazat
#ezt sikerült megoldani a legtrógerebben, igazából két for punciklussal nem keleltt volna ennyit ismételgetni, csak lusta vagyok :P
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 1) and (szavazat == egy)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n"% (kerulet,vezeteknev,keresztnev,part))
        text_file.close()
        
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 2) and (szavazat == ketto)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()  
        
        
    
            
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 3) and (szavazat == harom)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()            
    
                
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 4) and (szavazat == negy)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()                
    
                    
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 5) and (szavazat == ot)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()                    
    
                        
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 6) and (szavazat == hat)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()                        
    
                            
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 7) and (szavazat == het)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()                            
    
                                
for i in range(0,len(array)):
    kerulet = int(array[i][0])
    szavazat = int(array[i][1])
    vezeteknev=array[i][2]
    keresztnev=array[i][3]
    part=array[i][4]
    if(part == "-"):
        part = "független"
    if((kerulet == 8) and (szavazat == nyolc)):
        with open("kepviselok2.txt", "a") as text_file: #mert most nem write hanem append - csatol - ellenben az egszet elölről kezdené el.
             text_file.write("%d %s %s %s \n" % (kerulet,vezeteknev,keresztnev,part))
        text_file.close()                                
    
                                    
                                    
#%% MEGOLDASOK PONTSZAMAI
"""
valasztas néven létrehozott egy szintaktikailag helyes
programot 1 pont
A képernyőn minden megoldott feladat esetén megjelenik az
aktuális feladat száma 1 pont
A bemeneti állomány feldolgozása és az adatok tárolása 5 pont
A képviselőjelöltek száma 2 pont
Egy képviselőjelölt szavazatainak száma 5 pont
A részvételi arány kiszámítása 5 pont
A pártokra leadott szavazatok aránya 8 pont
A legtöbb szavazatot kapott jelölt(ek) megkeresése 8 pont
A képviselők meghatározása 10 pont
Összesen: 45 pont
"""