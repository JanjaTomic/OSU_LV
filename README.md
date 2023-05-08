# OSU_LV
---LV1---
Zadatak 1.1 
Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je pla´cen
po radnom satu. Koristite ugra ¯ denu Python metodu input(). Nakon toga izraˇcunajte koliko
je korisnik zaradio i ispišite na ekran. Na kraju prepravite rješenje na naˇcin da ukupni iznos
izraˇcunavate u zasebnoj funkciji naziva total_euro.
Primjer:
Radni sati: 35 h
eura/h: 8.5
Ukupno: 297.5 eura

Zadatak 1.2 
Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
nekakvu ocjenu i nalazi se izme ¯ du 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju
sljede´cih uvjeta:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
Takod¯er, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuc´u poruku.

Zadatak 1.3 
Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji
sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
(npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovarajucu poruku.
Zadatak 1.4.4 Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva song.txt.
Potrebno je napraviti rjecnik koji kao kljuˇceve koristi sve razlicite rijeci koje se pojavljuju u
datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (kljuc) pojavljuje u datoteci.
Koliko je rijeˇci koje se pojavljuju samo jednom u datoteci? Ispišite ih.

Zadatak 1.5 
Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva SMSSpamCollection.txt
[1]. Ova datoteka sadrži 5574 SMS poruka pri ˇcemu su neke oznaˇcene kao spam, a neke kao ham.
Primjer dijela datoteke:
ham Yup next stop.
ham Ok lar... Joking wif u oni...
spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
a) Izraˇcunajte koliki je prosjeˇcan broj rijeˇci u SMS porukama koje su tipa ham, a koliko je
prosjeˇcan broj rijeˇci u porukama koje su tipa spam.
b) Koliko SMS poruka koje su tipa spam završava uskliˇcnikom ?


---LV2---
Zadatak 2.1
 Pomocu funkcija numpy.array i matplotlib.pyplot pokušajte nacrtati sliku
2.3 u okviru skripte zadatak_1.py. Igrajte se sa slikom, promijenite boju linija, debljinu linije i
sl.

Zadatak 2.2
 Datoteka data.csv sadrži mjerenja visine i mase provedena na muškarcima i
ženama. Skripta zadatak_2.py ucitava dane podatke u obliku numpy polja data pri  cemu je u
prvom stupcu polja oznaka spola (1 muško, 0 žensko), drugi stupac polja je visina u cm, a tre´ci
stupac polja je masa u kg.
a) Na temelju velicine numpy polja data, na koliko osoba su izvršena mjerenja?
b) Prikažite odnos visine i mase osobe pomocu naredbe matplotlib.pyplot.scatter.
c) Ponovite prethodni zadatak, ali prikažite mjerenja za svaku pedesetu osobu na slici.
d) Izracunajte i ispišite u terminal minimalnu, maksimalnu i srednju vrijednost visine u ovom
podatkovnom skupu.
e) Ponovite zadatak pod d), ali samo za muškarce, odnosno žene. Npr. kako biste izdvojili
muškarce, stvorite polje koje zadrži bool vrijednosti i njega koristite kao indeks retka.
ind = (data[:,0] == 1)

Zadatak 2.3 
Skripta zadatak_3.py ucitava sliku ’road.jpg’. Manipulacijom odgovaraju´ce
numpy matrice pokušajte:
a) posvijetliti sliku,
--(potamniti: sub_brightness = 50
dark_img = np.where(img < sub_brightness, 0, img-sub_brightness)
b) prikazati samo drugu  cetvrtinu slike po širini,
c) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
--(zarotirati za bilokoji stupanj:
from scipy.ndimage import rotate
rotated = rotate(img, angle=45, reshape=False,mode='nearest')
plt.title("Rotirano za 47°")
plt.imshow(rotated, cmap="gray")
plt.show()
)
d) zrcaliti sliku.
--(axis=0 za zrcaliti po x osi)

Zadatak 2.
 Napišite program koji ce kreirati sliku koja sadrži cetiri kvadrata crne odnosno
bijele boje (vidi primjer slike 2.4 ispod). Za kreiranje ove funkcije koristite numpy funkcije
zeros i ones kako biste kreirali crna i bijela polja dimenzija 50x50 piksela. Kako biste ih složili
u odgovarajuci oblik koristite numpy funkcije hstack i vstack.

---LV3--
Zadatak 3.1 
Skripta zadatak_1.py ucitava podatkovni skup iz data_C02_emission.csv.
Dodajte programski kod u skriptu pomo´cu kojeg možete odgovoriti na sljedeca pitanja:
a) Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicina? Postoje li izostale ili
duplicirane vrijednosti? Obrišite ih ako postoje. Kategoricke velicine konvertirajte u tip
category.

b) Koja tri automobila ima najvecu odnosno najmanju gradsku potrošnju? Ispišite u terminal:
ime proizvodaca, model vozila i kolika je gradska potrošnja.

c) Koliko vozila ima velicinu motora izmedu 2.5 i 3.5 L? Kolika je prosjecna C02 emisija
plinova za ova vozila?

d) Koliko mjerenja se odnosi na vozila proizvodaca Audi? Kolika je prosjecna emisija C02
plinova automobila proizvodaca Audi koji imaju 4 cilindara?

e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecna emisija C02 plinova s obzirom na
broj cilindara?

f) Kolika je prosjecna gradska potrošnja u slucaju vozila koja koriste dizel, a kolika za vozila
koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?

g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvecu gradsku potrošnju goriva?

h) Koliko ima vozila ima rucni tip mjenjaca (bez obzira na broj brzina)?

i) Izracunajte korelaciju izmedu numerickih velicina. Komentirajte dobiveni rezultat.


Zadatak 3.2 
#Make,Model,Vehicle Class,Engine Size (L),Cylinders,Transmission,Fuel Type,Fuel Consumption City (L/100km)
#Fuel Consumption Hwy (L/100km),Fuel Consumption Comb (L/100km),Fuel Consumption Comb (mpg),CO2 Emissions (g/km)
Napišite programski kod koji ce prikazati sljedece vizualizacije:
a) Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz.

b) Pomocu dijagrama raspršenja prikažite odnos izmedu gradske potrošnje goriva i emisije
C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu
velicina, obojite tockice na dijagramu raspršenja s obzirom na tip goriva.

c) Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip
goriva. Primjecujete li grubu mjernu pogrešku u podacima?

d) Pomocu stupcastog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu
groupby.

e) Pomocu stupcastog grafa prikažite na istoj slici prosjecnu C02 emisiju vozila s obzirom na
broj cilindara.


---LV4---
Zadatak 4.1 Skripta zadatak_1.py ucitava podatkovni skup iz data_C02_emission.csv.
Potrebno je izgraditi i vrednovati model koji procjenjuje emisiju C02 plinova na temelju ostalih
numerickih ulaznih veliˇcina. Detalje oko ovog podatkovnog skupa mogu se prona´ci u 3.
laboratorijskoj vježbi.
a) Odaberite željene numericke velicine specificiranjem liste s nazivima stupaca. Podijelite
podatke na skup za ucenje i skup za testiranje u omjeru 80%-20%.

b) Pomo´cu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova
o jednoj numerickoj velicini. Pri tome podatke koji pripadaju skupu za ucenje oznacite
plavom bojom, a podatke koji pripadaju skupu za testiranje oznacite crvenom bojom.

c) Izvršite standardizaciju ulaznih velicina skupa za ucenje. Prikažite histogram vrijednosti
jedne ulazne velicine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja
transformirajte ulazne velicine skupa podataka za testiranje.

d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
povežite ih s izrazom 4.6.

e) Izvršite procjenu izlazne velicine na temelju ulaznih velicina skupa za testiranje. Prikažite
pomocu dijagrama raspršenja odnos izmedu stvarnih vrijednosti izlazne velicine i procjene
dobivene modelom.

f) Izvršite vrednovanje modela na nacin da izracunate vrijednosti regresijskih metrika na
skupu podataka za testiranje.

g) Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj
ulaznih velicina?

Zadatak 4.2 
Na temelju rješenja prethodnog zadatka izradite model koji koristi i kategoriˇcku
varijable „Fuel Type“ kao ulaznu velicinu. Pri tome koristite 1-od-K kodiranje kategorickih
velicina. Radi jednostavnosti nemojte skalirati ulazne velicine. Komentirajte dobivene rezultate.
Kolika je maksimalna pogreška u procjeni emisije C02 plinova u g/km? O kojem se modelu
vozila radi?


---LV5---
Zadatak 5.1 
Skripta zadatak_1.py generira umjetni binarni klasifikacijski problem s dvije
ulazne veliˇcine. Podaci su podijeljeni na skup za ucenje i skup za testiranje modela.
a) Prikažite podatke za ucenje u x1−x2 ravnini matplotlib biblioteke pri cemu podatke obojite
s obzirom na klasu. Prikažite i podatke iz skupa za testiranje, ali za njih koristite drugi
marker (npr. ’x’). Koristite funkciju scatter koja osim podataka prima i parametre c i
cmap kojima je mogu´ce definirati boju svake klase.

b) Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka
za ucenje.

c) Pronadite u atributima izgradenog modela parametre modela. Prikažite granicu odluke
naucenog modela u ravnini x1 −x2 zajedno s podacima za ucenje. Napomena: granica
odluke u ravnini x1−x2 definirana je kao krivulja: θ0+θ1x1+θ2x2 = 0.

d) Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke
regresije. Izracunajte i prikažite matricu zabune na testnim podacima. Izracunate tocnost,
preciznost i odziv na skupu podataka za testiranje.

e) Prikažite skup za testiranje u ravnini x1−x2. Zelenom bojom oznacite dobro klasificirane
primjere dok pogrešno klasificirane primjere oznacite crnom bojom.


Zadatak 5.2 
Skripta zadatak_2.py ucitava podatkovni skup Palmer Penguins [1]. Ovaj
podatkovni skup sadrži mjerenja provedena na tri razlicite vrste pingvina (’Adelie’, ’Chinstrap’,
’Gentoo’) na tri razlicita otoka u podrucju Palmer Station, Antarktika. Vrsta pingvina
odabrana je kao izlazna velicina i pri tome su klase oznacene s cjelobrojnim vrijednostima
0, 1 i 2. Ulazne veliˇcine su duljina kljuna (’bill_length_mm’) i duljina peraje u mm (’flipper_
length_mm’). Za vizualizaciju podatkovnih primjera i granice odluke u skripti je dostupna
funkcija plot_decision_region.

a) Pomocu stupcastog dijagrama prikažite koliko primjera postoji za svaku klasu (vrstu
pingvina) u skupu podataka za ucenje i skupu podataka za testiranje. Koristite numpy
funkciju unique.

b) Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka
za ucenje.

c) Pronadite u atributima izgradenog modela parametre modela. Koja je razlika u odnosu na
binarni klasifikacijski problem iz prvog zadatka?

d) Pozovite funkciju plot_decision_region pri cemu joj predajte podatke za uˇcenje i
izgrad¯eni model logisticˇke regresije. Kako komentirate dobivene rezultate?

e) Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticˇke
regresije. Izraˇcunajte i prikažite matricu zabune na testnim podacima. Izraˇcunajte toˇcnost.
Pomo´cu classification_report funkcije izracunajte vrijednost cetiri glavne metrike na skupu podataka za testiranje.

f) Dodajte u model još ulaznih veliˇcina. Što se doga ¯ da s rezultatima klasifikacije na skupu
podataka za testiranje?


---LV6---

Zadatak 6.1
 Skripta zadatak_1.py ucitava Social_Network_Ads.csv skup podataka [2].
Ovaj skup sadrži podatke o korisnicima koji jesu ili nisu napravili kupovinu za prikazani oglas.
Podaci o korisnicima su spol, dob i procijenjena pla´ca. Razmatra se binarni klasifikacijski
problem gdje su dob i procijenjena pla´ca ulazne veliˇcine, dok je kupovina (0 ili 1) izlazna
veliˇcina. Za vizualizaciju podatkovnih primjera i granice odluke u skripti je dostupna funkcija
plot_decision_region [1]. Podaci su podijeljeni na skup za uˇcenje i skup za testiranje modela
u omjeru 80%-20% te su standardizirani. Izgra ¯ den je model logistiˇcke regresije te je izraˇcunata
njegova toˇcnost na skupu podataka za uˇcenje i skupu podataka za testiranje. Potrebno je:
1. Izradite algoritam KNN na skupu podataka za uˇcenje (uz K=5). Izraˇcunajte toˇcnost
klasifikacije na skupu podataka za uˇcenje i skupu podataka za testiranje. Usporedite
dobivene rezultate s rezultatima logistiˇcke regresije. Što primje´cujete vezano uz dobivenu
granicu odluke KNN modela?
2. Kako izgleda granica odluke kada je K =1 i kada je K = 100?

Zadatak 6.5.2 
Pomo´cu unakrsne validacije odredite optimalnu vrijednost hiperparametra K
algoritma KNN za podatke iz Zadatka 1.

Zadatak 6.5.3 
Na podatke iz Zadatka 1 primijenite SVM model koji koristi RBF kernel funkciju
te prikažite dobivenu granicu odluke. Mijenjajte vrijednost hiperparametra C i γ. Kako promjena
ovih hiperparametara utjeˇce na granicu odluke te pogrešku na skupu podataka za testiranje?
Mijenjajte tip kernela koji se koristi. Što primje´cujete?

Zadatak 6.5.4
 Pomocu unakrsne validacije odredite optimalnu vrijednost hiperparametra C i γ
algoritma SVM za problem iz Zadatka 1.
--(print(svm_gscv.best_score_)
print(svm_gscv.cv_results_)


---LV7---
Zadatak 7.5.1 
Skripta zadatak_1.py sadrži funkciju generate_data koja služi za generiranje
umjetnih podatkovnih primjera kako bi se demonstriralo grupiranje. Funkcija prima cijeli broj
koji definira željeni broju uzoraka u skupu i cijeli broj od 1 do 5 koji definira na koji naˇcin ´ce
se generirati podaci, a vra´ca generirani skup podataka u obliku numpy polja pri cemu su prvi i
drugi stupac vrijednosti prve odnosno druge ulazne velicine za svaki podatak. Skripta generira
500 podatkovnih primjera i prikazuje ih u obliku dijagrama raspršenja.
1. Pokrenite skriptu. Prepoznajete li koliko ima grupa u generiranim podacima? Mijenjajte
naˇcin generiranja podataka.
2. Primijenite metodu K srednjih vrijednosti te ponovo prikažite primjere, ali svaki primjer
obojite ovisno o njegovoj pripadnosti pojedinoj grupi. Nekoliko puta pokrenite programski
kod. Mijenjate broj K. Što primjecujete?
3. Mijenjajte nacin definiranja umjetnih primjera te promatrajte rezultate grupiranja podataka
(koristite optimalni broj grupa). Kako komentirate dobivene rezultate?

Zadatak 7.5.2
 Kvantizacija boje je proces smanjivanja broja razlicitih boja u digitalnoj slici, ali
uzimaju´ci u obzir da rezultantna slika vizualno bude što sliˇcnija originalnoj slici. Jednostavan
naˇcin kvantizacije boje može se postici primjenom algoritma K srednjih vrijednosti na RGB
vrijednosti elemenata originalne slike. Kvantizacija se tada postiže zamjenom vrijednosti svakog
elementa originalne slike s njemu najbližim centrom. Na slici 7.3a dan je primjer originalne
slike koja sadrži ukupno 106,276 boja, dok je na slici 7.3b prikazana rezultantna slika nakon
kvantizacije i koja sadrži samo 5 boja koje su odred¯ene algoritmom K srednjih vrijednosti.
1. Otvorite skriptu zadatak_2.py. Ova skripta uˇcitava originalnu RGB sliku test_1.jpg
te ju transformira u podatkovni skup koji dimenzijama odgovara izrazu 7.2 pri cemu je n
broj elemenata slike, a m je jednak 3. Koliko je razlicitih boja prisutno u ovoj slici?
2. Primijenite algoritam K srednjih vrijednosti koji ce pronaci grupe u RGB vrijednostima
elemenata originalne slike.
3. Vrijednost svakog elementa slike originalne slike zamijeni s njemu pripadaju´cim centrom.
4. Usporedite dobivenu sliku s originalnom. Mijenjate broj grupa K. Komentirajte dobivene
rezultate.
5. Primijenite postupak i na ostale dostupne slike.
6. Graficki prikažite ovisnost J o broju grupa K. Koristite atribut inertia objekta klase
KMeans. Možete li uociti lakat koji upucuje na optimalni broj grupa?
7. Elemente slike koji pripadaju jednoj grupi prikažite kao zasebnu binarnu sliku. Što
primje´cujete?


---LV8---
Zadatak 8.4.1 
MNIST podatkovni skup za izgradnju klasifikatora rukom pisanih znamenki
dostupan je u okviru Keras-a. Skripta zadatak_1.py ucitava MNIST podatkovni skup te podatke
priprema za ucenje potpuno povezane mreže.
1. Upoznajte se s ucitanim podacima. Koliko primjera sadrži skup za ucenje, a koliko skup za
testiranje? Kako su skalirani ulazni podaci tj. slike? Kako je kodirana izlazne velicina?
2. Pomocu matplotlib biblioteke prikažite jednu sliku iz skupa podataka za ucenje te ispišite
njezinu oznaku u terminal.
3. Pomocu klase Sequential izgradite mrežu prikazanu na slici 8.5. Pomo´cu metode
.summary ispišite informacije o mreži u terminal.
4. Pomocu metode .compile podesite proces treniranja mreže.
5. Pokrenite ucenje mreže (samostalno definirajte broj epoha i veliˇcinu serije). Pratite tijek
ucenja u terminalu.
6. Izvršite evaluaciju mreže na testnom skupu podataka pomo´cu metode .evaluate.
7. Izracunajte predikciju mreže za skup podataka za testiranje. Pomo´cu scikit-learn biblioteke
prikažite matricu zabune za skup podataka za testiranje.
8. Pohranite model na tvrdi disk.

Zadatak 8.4.2 
Napišite skriptu koja ce ucitati izgradenu mrežu iz zadatka 1 i MNIST skup
podataka. Pomocu matplotlib biblioteke potrebno je prikazati nekoliko loše klasificiranih slika iz
skupa podataka za testiranje. Pri tome u naslov slike napišite stvarnu oznaku i oznaku predvid¯enu
mrežom.


Zadatak 8.4.3 
Napišite skriptu koja ce ucitati izgradenu mrežu iz zadatka 1. Nadalje, skripta
treba ucitati sliku test.png sa diska. Dodajte u skriptu kod koji ce prilagoditi sliku za mrežu,
klasificirati sliku pomocu izgradene mreže te ispisati rezultat u terminal. Promijenite sliku
pomocu nekog grafickog alata (npr. pomo´cuWindows Paint-a nacrtajte broj 2) i ponovo pokrenite
skriptu. Komentirajte dobivene rezultate za razliˇcite napisane znamenke.



---LV9---

Zadatak 9.4.1 
Skripta Zadatak_1.py ucitava CIFAR-10 skup podataka. Ovaj skup sadrži
50000 slika u skupu za uˇcenje i 10000 slika za testiranje. Slike su RGB i rezolucije su 32x32.
Svakoj slici je pridružena jedna od 10 klasa ovisno koji je objekt prikazan na slici. Potrebno je:
1. Prouˇcite dostupni kod. Od kojih se slojeva sastoji CNN mreža? Koliko ima parametara
mreža?
2. Pokrenite ucenje mreže. Pratite proces ucenja pomocu alata Tensorboard na sljede´ci naˇcin.
Pokrenite Tensorboard u terminalu pomo´cu naredbe:
tensorboard –logdir=logs
i zatim otvorite adresu http://localhost:6006/ pomocu web preglednika.
3. Proucite krivulje koje prikazuju tocnost klasifikacije i prosjecnu vrijednost funkcije gubitka
na skupu podataka za ucenje i skupu podataka za validaciju. Što se dogodilo tijekom uˇcenja
mreže? Zapišite tocnost koju ste postigli na skupu podataka za testiranje.

Zadatak 9.4.2 
Modificirajte skriptu iz prethodnog zadatka na nacin da na odgovarajuca mjesta u
mrežu dodate droput slojeve. Prije pokretanja ucenja promijenite Tensorboard funkciju povratnog
poziva na nacin da informacije zapisuje u novi direktorij (npr. =/log/cnn_droput). Pratite tijek
ucenja. Kako komentirate utjecaj dropout slojeva na performanse mreže?

Zadatak 9.4.3
 Dodajte funkciju povratnog poziva za rano zaustavljanje koja ce zaustaviti proces
ucenja nakon što se 5 uzastopnih epoha ne smanji prosjeˇcna vrijednost funkcije gubitka na
validacijskom skupu.

Zadatak 9.4.4 
Što se dogad¯a s procesom ucenja:
1. ako se koristi jako velika ili jako mala velicina serije?
2. ako koristite jako malu ili jako veliku vrijednost stope ucenja?
3. ako izbacite odredene slojeve iz mreže kako biste dobili manju mrežu?
4. ako za 50% smanjite velicinu skupa za ucenje?
