Model-Template-View
===========================================

Django sledi tako imenovani `*Model-View-Controller* <http://en.wikipedia.org/wiki/Model–view–controller>`_ filozofiji, kar pomeni, da so aplikacije zasnovane tako, da imamo čisto ločitev podatkovne baze (*Model*), aplikativne logike (*Controller*) in izrisovalnih predlog (*View*). To pomaga ohranjati kodo čisto in brez grdih *hackov* in predloge brez aplikativne logike (in posledično veliko bolj prijazne očem oblikovalcev).

Striktno gledano se Django opredeljuje kot MTV oz. Model-Template-View, pri čemer Template služi kot View in View kot kontroler. Takšno poimenovanje se uporablja tudi v Django-tovi dokumentaciji in ker je za vse praktične namene ekvivalentno MVC, bomo za namene zmanjšanja zmešnjave ob obračanju na uradno dokumentacijo sledili Django-tovemu poimenovanju.

Bojni načrt
-----------

Odločili smo se, da potrebuje naša homepatska lekarna poleg spletne trgovine tudi možnost objavljanja člankov, ki bodo v pomoč našim kupcem pri reševanju njihovih tegob.

Podatkovna baza - Model
-----------------------

Najprej nam bo v pomoč razbiti naš problem na manjše podprobleme. Očitno bomo morali prikazovati članke, za kar bo skrbel naš *View* s svojo aplikativno logiko, a le-tega še ne rabimo takoj sprogramirati, saj moramo pred prikazom člankov le-te shraniti.

(*Samo kreiranje projekta in nove aplikacije na te mestu še ni pomembno in lahko še počaka nekaj minut.*)

Preden pa jih shranimo pa je potrebno tudi premisliti katere vse podatke potrebujemo in v kakšnem formatu jih bomo shranili, kar načrtujemo v našem model-u.::

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