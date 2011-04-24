Preden začnemo
==============

Da lahko sledimo tej delavnici, potrebujemo (kako presenetljivo) Django, ki je napisan v Python-u, nima pa kakšnih zunanjih odvisnosti (boste pa morali sami namestiti katero izmed boljših podatkovnih baz, če boste potrebovali njene zmogljivosti)

Kljub že nekaj časa trajajočemu prehodu na Python 3, Django še ne podpira Python 3, predvsem zato, ker je Python 3 prinesel nekaj nekompatibilnih sprememb med 2.x in 3.0, tako da bo prehod trajal še nekaj časa, saj je potrebno opustiti podporo za vejo 2.x preden lahko preidemo na 3.x.

Za večino vsakdanjih operacij ostajanje na 2.x ne bo pomenilo večjih sprememb, saj so vse omembe vredne knjižice še vedno kompatibilnih z 2.x.

Python
------

Windows
^^^^^^^
`Obiščite Python-ovo spletno stran in si prenesite ustrezno različico 2.7 veje (obstajata 32 in 64 bitna različica)  <http://www.python.org/getit/>`_.

Mac OS X in Linux
^^^^^^^^^^^^^^^^^
Python je že nameščen.


Django
------

Obiščite `uradno stran <http://www.djangoproject.com/download/>`_ in si prenesite trenutno stabilno različico. Če ste na Linux-u ali Mac-u, lahko sledite priloženim navodilom za razširitev kompresirane vsebine in namestitev Django-ta::

    tar xzvf Django-NNN.tar.gz
    cd Django-NNN
    sudo python setup.py install 

Če pa uporabljate Windows-e, boste morali uporabiti orodje kot je 7-zip ali bsdtar za odpakiranje, nakar zaženite ukazno vrstico z administrativnimi privilegiji in poženite ukaz::
    
    setup.py install
