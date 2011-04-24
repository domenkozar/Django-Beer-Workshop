Model
===========================

Najprej nam bo v pomoč razbiti naš problem na manjše podprobleme. Očitno bomo morali prikazovati članke, za kar bo skrbel naš *View* s svojo aplikativno logiko, a le-tega še ne rabimo takoj sprogramirati, saj moramo pred prikazom člankov le-te shraniti.

(*Samo kreiranje projekta in nove aplikacije na te mestu še ni pomembno in lahko še počaka nekaj minut.*)

Preden pa jih shranimo pa je potrebno tudi premisliti katere vse podatke potrebujemo in v kakšnem formatu jih bomo shranili, kar načrtujemo v našem modelu.::

    class Reporter(models.Model):
       full_name = models.CharField(max_length=70)

       def __unicode__(self):
          return self.full_name

    class Article(models.Model):
       pub_date = models.DateTimeField()
       headline = models.CharField(max_length=200)
       content = models.TextField()
       reporter = models.ForeignKey(Reporter)

       def __unicode__(self):
          return self.headline
          
Ker Django uporablja ORM (`Object-relational mapping <http://en.wikipedia.org/wiki/Object-relational_mapping>`_) dostop do podatkovne baze, predstavimo tabele kot objekte, katerih atributi so stolpci v tabelah, vrstice v tabelah pa so instance teh objektov.

V našem primeru smo tako razredu Reporter (novinar) dodali le atribut full_name (polno ime) in mu podali najdaljšo dolžino le-tega, razredu Article (članek) pa smo dali atribute datuma objave, naslova, vsebino in kateri novinar ga je napisal.

Naslednji korak je te tabele dodati tudi v samo podatkovono bazo, kar storimo z ukazom::

    python manage.py syncdb
    
Ko Django za nas ustvari tabele se lahko zabava začne.

Dostop do podatkovne baze
-------------------------

Do podatkovne baze lahko dostopamo na dva načina - prvi je, da preko Django-tovega ORM API-ja dostopamo do same baze iz naše aplikacije, drugi pa, da uporabimo Django-tov *shell*, ki je v bistvu Python-ova ukazna vrstica, ki jo Django samodejno *poseli* z ORM API-jem, kar nam omogoča hitro preizkušanje naših zahtevkov.

Za začetno predstavo si torej poglejmo kaj lahko naredimo z ukazno vrstico::

    python manage.py shell
    
Prikaže se ukazna vrstica, v katero najprej vključimo naše modele::

    In [1]: from newsroom.articles.models import Article, Reporter

    In [2]: Article.objects.all()
    Out[2]: []

Vidimo, da je naša demonstrativna aplikacija z imenom articles uspešno naložila modele, ki so v tej fazi projekta še prazni. Zatorej dodajmo najprej nekaj novinarjev...::

    In [3]: r = Reporter(full_name="Janez Novak")

    In [4]: r.save()

    In [5]: r.id
    Out[5]: 1

    In [6]: Reporter.objects.all()
    Out[6]: [<Reporter: Janez Novak>]
    
Kot je precej očitno iz kode smo dodali v podatkovno bazo nov objekt z imenom Janez Novak, ga shranili in po shranitvi pogledali, kakšen je njegov unikatni identifikator. Poglejmo si nekaj načinov, kako lahko do teh podatkov sedaj tudi dostopamo...::
    
    In [10]:Reporter.objects.get(startswith="Janez")
    Out[11]: <Reporter: Janez Novak>
    
    In [32]: Reporter.objects.get(full_name__contains='ane')
    Out[32]: <Reporter: Janez Novak>
    
Z dvojnim podčrtajem lahko izvajamo poizvedbe na pojmih (angleško *field lookups*), ki se prevedejo v srce WHERE izjave v SQL-u.

.. note::
    Če ste kdaj že videli Python, vam bo morda sintaksa ``field__lookuptype=value`` delovala nekoliko čudno in se boste spraševali kako je to mogoče. Python ima možnost definirati funkcije, ki sprejmejo poljubno število ``name-value`` argumentov, katerih imena in vrednosti so evaluirani ob izvršitvi. Za več informacij si poglejte `Keyword Arguments <http://docs.python.org/tutorial/controlflow.html#keyword-arguments>`_ v Python-ovi dokumentaciji.
    
Sedaj lahko ustvarimo tudi prvi članek.::

    In [46]: a = Article(pub_date=datetime.datetime.now(), headline="Nove droge!", content="Dobili smo sveo poiljko domaih zdravil, oglasite se na preizkunji", reporter=r)

    In [47]: a.save()

    In [48]: Article.objects.all()
    Out[48]: [<Article: Nove droge!>]
    
Nič posebej novega zaenkrat...::

    In [49]: r
    Out[49]: <Reporter: Janez Novak>

    In [50]: a.reporter
    Out[50]: <Reporter: Janez Novak>
    
Z klicanjem metod na naši instanci smo torej prišli do objekta Reporter, ki je ustvaril članek.::

    In [51]: r.article_set.all()
    Out[51]: [<Article: Nove droge!>]
    
Obratno lahko z klicanjem ``article_set`` (ker obstaja velika verjetnost, da je novinar napisal več člankov, imamo očitno opravka z ``set`` strukturo) vidimo seznam vseh člankov.::

    In [53]: Article.objects.filter(reporter__full_name__startswith="Janez")
    Out[53]: [<Article: Nove droge!>]

API bo sledil relacijam kakor globoko je potrebno, pri čemer bo sam izvajal učinkovite JOIN operacije.

.. note::
    Omeniti velja, da so vse operacije na podatkovnih objektih *lene*, kar pomeni, da se bodo izvršile šele ko bo to res potrebno. Tako lahko mirne vesti dodajamo dodatne ``filter``, ``exclude``, ga "razrežemo" in izvajamo vrsto drugih operacij, pa Django ne bo izvršil SQL operacije dokler to res ne bo to potrebno (npr. za izris).

Objekte lahko spreminjamo preprosto s spreminjem atributov: ::
    
    In [54]: r.full_name = "Urban Skudnik"

    In [55]: r.save
    Out[55]: <bound method Reporter.save of <Reporter: Urban Skudnik>>

    In [56]: r.save()

    In [57]: r
    Out[57]: <Reporter: Urban Skudnik>
    
Za konec si lahko pogledamo še vse metode in atribute, ki jih imajo naši objekti:

.. note::
    Funkcija ``dir([object])`` poskuša (na več načinov) priskrbeti informacije o dostopnih metodah in atributih.

::
    
    In [58]: dir(r)
    Out[58]: 
    ['DoesNotExist',
    'MultipleObjectsReturned',
    '__class__',
    '__delattr__',
    '__dict__',
    '__doc__',
    '__eq__',
    '__format__',
    '__getattribute__',
    '__hash__',
    '__init__',
    '__metaclass__',
    '__module__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    '__unicode__',
    '__weakref__',
    '_base_manager',
    '_default_manager',
    '_deferred',
    '_get_FIELD_display',
    '_get_next_or_previous_by_FIELD',
    '_get_next_or_previous_in_order',
    '_get_pk_val',
    '_get_unique_checks',
    '_meta',
    '_perform_date_checks',
    '_perform_unique_checks',
    '_set_pk_val',
    '_state',
    '**article_set**',
    'clean',
    'clean_fields',
    'date_error_message',
    '**delete**',
    'full_clean',
    '**full_name**',
    '**id**',
    'objects',
    'pk',
    'prepare_database_save',
    '**save**',
    'save_base',
    'serializable_value',
    'unique_error_message',
    'validate_unique']


Metode, ki se začnejo in končajo z dvojnim podčrtajem (``__imemetode__``) so zasebne metode, s katerimi se načeloma ne operira (funkcija ``dir`` npr. sama pregleda, če objekt implementira metodo ``__dir__()``, sicer poskuša sestaviti najboljšo sliko iz informacij, ki so shranjene v ``__dict()``) in se na njih naj ne bi zanašali. Te podrobnosti pa spadajo že v naprednejše poglavje Python-a in so na tej točki nepotrebne. 

Lahko pa se sedaj lotimo naslednjega koraka - Django-tovega administrativnega vmesnika, s katerim lahko hitro in v grafični obliki dodajamo podatke.

Administrativni vmesnik
-----------------------

Potem ko smo definirali modele za aplikacijo, je vključitev administrativnega vmesnika otročje lahka - v ``admin.py``, ki je v istem direktoriju kot models.py registriramo naš model: ::

    import models
    from django.contrib import admin

    admin.site.register(models.Article)

Projektno gledano moramo sicer vklopiti administrativni vmesnik še v nastavitvah in pri URL konfiguraciji, a do tega pridemo nekoliko kasneje.