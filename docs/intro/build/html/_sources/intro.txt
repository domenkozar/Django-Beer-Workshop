O Django-tu
===========================================

Kaj je Django?
--------------

    `Django <http://en.wikipedia.org/wiki/Django_(Web_framework)>`_ je visoko-nivojsko `Python <http://python.org>`_ spletno ogrodje, ki spodbuja hiter razvoj in čisto zasnovo in je v razvoju že več štiri leta v spletnem uredništvu `Lawrence Journal-World-a <http://www.ljworld.com/>`_ in je bilo julija 2005 dano v javnost pod BSD licenco.

    Django je bil zasnovan z dvema izivoma v mislih - stresnimi razmerami novinarskih sob in strogimi zahtevami izkušenih razvijalcev, ki so ga tudi razvili. Pri tem poskuša avtomatizirati kar se da veliko za spletne razmere pogostih operacij (`caching <http://docs.djangoproject.com/en/1.3/topics/cache/>`_, `ponujanje vsebine - syndication <http://docs.djangoproject.com/en/dev/ref/contrib/syndication/?from=olddocs>`_, `komentiranje <http://docs.djangoproject.com/en/dev/ref/contrib/comments/>`_, itd.) in sledi `DRY (Don't Repeat Yourself - ne ponavljaj se) <http://c2.com/cgi/wiki?DontRepeatYourself>`_ principu.
    
    Django ni sistem za upravljanje vsebine (CMS - Content Management System) sam po sebi in ga ne moremo uporabljati kot rešitev na ključ. Je spletno ogrodje, s katerim lahko razvijemo spletne strani. Tako da nima smisla primerjati z Plone-om ali Drupal-om, ker je Django orodje, s katerim bi kvečjemu razvil kaj takšnega. 

    Kljub temu pa ima Django marsikatero značilnost, s katero se olajša razvoj CMS strani - napredna administrativna plošča za izbrane modele je samo ena izmed takšnih značilnosti.
    
Ampak, kaj je "Django"?
-----------------------

    Django je poimenovan po `Django Reinhardt-u <http://en.wikipedia.org/wiki/Django_Reinhardt>`_, romskemu kitaristu, ki se še danes smatra za enega izmed najboljših kitaristov na svetu.
    
Je Django stabilen?
-------------------

`Da. <http://www.djangosites.org/>`_

Ali se Django skalira?
----------------------

Da. Django ima t.i. "deli-nič" arhitekturo, kar pomeni, da lahko dodatne strežnike dodamo na katerem koli nivoju, Django pa bo izkoristil vse strojno opremo, s katero mu lahko postrežemo, pri čemer loči komponente (podatkovna baza, aplikacijski nivo, ...).

Z ločenim strežnikom za podatkovno bazo, ločenim strežnikom za statično vsebino (ali uporabo `CDN - Content Delivery Network <http://en.wikipedia.org/wiki/Content_delivery_network>`_) in ločenim strežnikom za aplikativno logiko lahko Django odgovori na okoli 10 milijonov zahtevkov na dan, pri čemer je pametno, da se začnejo uporabljati tudi redudančni strežniki.

Django lahko, ob upoštevanju določenih specifik t.i. oblačnih storitev uporabimo tudi na Google App Engine-u, brez večjih problemov pa ga lahko uporabljamo tudi na Amazonovemu EC2.

Kdo razvija Django?
---------------------

Django so prvotno razvili v spletnem uredništvu World Online iz Lawrence, Kansas, ZDA, dandanes pa ga razvija mednarodna `ekipa prostovoljcev <http://docs.djangoproject.com/en/1.3/internals/committers/>`_.