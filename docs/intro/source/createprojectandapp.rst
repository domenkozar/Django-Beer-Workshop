V začetku je Bog ustvaril nebo in zemljo
========================================

Preden se lotimo pisanja model, moramo najprej ustvariti nov projekt, k kateremu bodo naše aplikacije pripadale.

Django nam bo pri tem pomagal z avtomatskim generiranjem kode, ki jo potrebuje osnovni projekt - projektne nastavitve, ki vsebujejo opcije za podatkovno bazo, ali projekt uporablja več jezikov (internacionalizacijske nastavitve), kje se nahajajo statične datoteke, kje so predloge, ipd. - v splošnem torej vse kar je specifično za Django ali aplikacije, ki jih uporabljamo.

Nov projekt ustvarimo z ukazom::

django-admin.py startproject tvseries

Ta ukaz bo ustvaril naslednjo direktorijsko strukturo::

    tvseries/
        __init__.py
        manage.py
        settings.py
        urls.py

Na kratko smo nekaj že omenili o teh datotekah, njihov pomen pa je očiten tudi iz njihovih imen:

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

    python manage.py startapp blog
    
kar ustvari sledečo datotečno strukturo::

    polls/
        __init__.py
        models.py
        tests.py
        views.py

