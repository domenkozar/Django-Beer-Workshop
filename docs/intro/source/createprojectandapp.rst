V začetku je Bog ustvaril nebo in zemljo
========================================

Preden se lotimo pisanja modelov, moramo najprej ustvariti nov projekt, h kateremu bodo naše aplikacije pripadale.

Django nam bo pri tem pomagal z avtomatskim generiranjem kode, ki jo potrebuje osnovni projekt - projektne nastavitve, ki vsebujejo opcije za podatkovno bazo, ali projekt uporablja več jezikov (internacionalizacijske nastavitve), kje se nahajajo statične datoteke, kje so predloge, ipd. - v splošnem torej vse kar je specifično za Django ali aplikacije, ki jih uporabljamo.

Nov projekt ustvarimo z ukazom::

django-admin.py startproject tvseries

Ta ukaz bo ustvaril naslednjo direktorijsko strukturo::

    tvseries/
        __init__.py
        manage.py
        settings.py
        urls.py

Na kratko smo nekaj že omenili te datoteke, njihov pomen pa je bolj ali manj očiten tudi iz njihovih imen:

* ``__init__.py``: Prazna datoteka, ki Python-u pove, da naj obravnava direktorij kot Python-ov paket. 
* ``manage.py``: Orodje za ukazno vrstico, ki omogoča delo z projektom
* ``settings.py``: Projektne nastavitve
* ``urls.py``: URL specifikacija

Razvijalski strežnik
--------------------

Django ima v svojem sklopu vključen tudi razvijalski strežnik, ki nam pomaga pri razvoju (nikakor pa ni primeren za produkcijsko rabo). Potem ko preidemo v ukazni vrstici v naš direktorij, ga z ukazom ``python manage.py runserver`` lahko poženemo. Z nekaj sreče bomo videli naslednji izpis::

    Validating models...
    0 errors found.

    Django version 1.0, using settings 'mysite.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
Django-tov vključen server je zelo preprost in spisan izključno v Python-u, njegov namen pa je pohitriti in olajšati razvoj, saj je konfiguriranje resnih strežnikov lahko mukotrpno in povsem nepotrebno za projekt, ki v začetni fazi nikakor ne potrebuje nepotrebnih zapletov.

Konfiguracija podatkovne baze
-----------------------------

Če se je naš projekt uspešno zagnal, lahko pred začetkom programiranja nastavimo še podatkovno bazo. V našem primeru bomo izbrali SQLite, lahko pa brez posežete tudi po naprednejših bazah kot so MySQL in PostGreSQL. 

V ``settings.py`` torej spremenimo ``ENGINE`` na 'django.db.backends.sqlite'.

Ker nekatere izmed že vključenih aplikacij (naštete so pod nastavitvijo ``INSTALLED_APPS``) potrebujejo podatkovno bazo, lahko le-to zapolnimo z tabelami z ukazom::

    python manage.py syncdb

Ukaz ``syncdb`` pogleda v ``INSTALLED_APPS`` ustvari potrebne podatkovne tabele, pri tem pa izpiše vse uspešno ustvarjene tabele in povpraša uporabnika, če želi ustvariti tudi administrativni račun.

Ustvarjenje aplikacije
----------------------

Potem ko smo zaključili s splošnimi projektnimi nastavitvami lahko nadaljujemo z ustvarjanjem svoje prve aplikacije. Vsaka aplikacija je, podobno kot sam projekt, svoj Python paket. Ustvarimo jo z ukazom::

    python manage.py startapp series
    
kar ustvari sledečo datotečno strukturo::

    series/
        __init__.py
        models.py
        tests.py
        views.py

Končno pa lahko nadaljujemo z zanimivejšim delom - zasnovanjem modelov.

Ker Django sledi principu DRY ("Don't repeat yourself"), je model edini vir podatkov o naših podatkih, kar pomeni da lahko na podlagi modela izpeljemo vrsto drugih stvari (na primer avtomatsko preverjanje pravilnosti formata podatkov, ki jih vnašamo v bazo).

Pred pisanjem samih modelov za začetek postojimo in najprej razmislimo o našem problemu. Če hočemo v našo videoteko shranjevati podatke o serijah, moramo torej shraniti podatke o seriji in njenih epizodah. To pomeni, da bomo imeli dve tabeli (eno Serie in drugo Episode).

Podatki o seriji, ki jih bomo shranili bodo unikatni identifikator, ime serije, IMDB unikatni identifikator in ocena same serije.

Vsaka epizoda, ki jo bomo shranili, bo pripadala eni seriji, kar pomeni da bomo morali ustvariti še 1:N relacijo v podatkovni bazi, poleg tega pa bomo shranili še ime, IMDB identifikator, oceno, številko epizode, številko serije in datum prvega predvajanja. 

Modela bosta torej izgledala tako::

    class Episode(models.Model):
        name = models.CharField(max_length=240)
        imdb_id = models.IntegerField('')
        rating = models.FloatField()
        episode_number = models.IntegerField()
        season_number = models.IntegerField()
        airdate = models.DateTimeField() # timezone? l10n?

        serie = models.ForeignKey('Serie')


    class Serie(models.Model):
        name = models.CharField(max_length=240)
        imdb_id = models.IntegerField('')
        rating = models.FloatField()
        poster = models.ImageField(upload_to="series")

Kljub očitnosti kode si poglejmo nekoliko podrobneje s čim imamo dejansko opravka.

Vsak model je predstavljen kot podrazred razreda ``django.db.models.Model`` in ima več spremenljivk, od katerih vsaka predstavlja polje v podatkovni bazi. Vsako polje je predstavljeno kot instanca razreda ``Field``, ki določi tip teh podatkov. Ime vsake instance ``Field-a`` pa je ime polja v računalniku prijazni obliki - mi bomo uporabljali to v naši aplikaciji, podatkovna baza pa kot ime stolpca v tabeli.

S prvim argumentom ``Field-u`` lahko podamo tudi ljudem prijaznejše oblike imen tabel, ki se bodo prikazovali v administrativnem vmesniku in obrazcih. 

Nekatera polja razreda ``Field`` imajo obvezne parametre, ki pa se ne uporabljajo zgolj v shemi podatkovne baze, ampak tudi za preverjanje podatkov, preden se vpišejo v podatkovno bazo. 

``ForeignKey`` predstavlja našo relacijo pripadanja epizode eni seriji.

Z temi podatki je Django sposoben izdelati shemo podatkovne baze in Python API za dostop do Episode in Serie objektov. Preden pa lahko naš model dejansko uporabimo, moramo našo aplikacijo še dodati med nameščene aplikacije (``INSTALLED_APPS``) v nastavitvah.

Tako odpremo datoteko ``settings.py`` in v ``INSTALLED_APPS`` dodamo na koncu ``series`` (ne pozabiti dodati vejco na konec prejšnje vrstice) in ponovno poženemo ukaz::

    python manage.py syncdb

``syncdb`` bo ustvaril tabele aplikacij, ki prej še niso bile uporabljene, za le-te pa bo tudi uvozil podatke in ustvaril indekse. Če hočemo spremeniti tabele, ki že obstajajo, pa je potrebno ali ročno spremeniti bazo ali pa poseči po orodjih, kot je south. 