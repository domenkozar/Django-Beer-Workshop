View & Template
===============

Lepi URL-ji
-----------

Že dolgo se od spletne aplikacije zahteva še kaj več kot samo lep prikaz informacij in uporaba lepih in predvsem uporabnih URL-jev je prvi korak v tem procesu.

Za načrtovanje svojih URL-jev moramo ustvari lasten URLconf modul, ki predstavlja stvarno kazalo med URL vzorci, na katerih bo dostopna vsebina in Python funkcijami, ki bodo do vsebino dejansko dostavile.

Če nadaljujemo z našim primerom: ::

    urlpatterns = patterns('',
        (r'^articles/(\d{4})/$', 'news.views.year_archive'),
        (r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
        (r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),
    )
    
Prav tako pa bi lahko dodali še vrstico ``url(r'^admin/', include(admin.site.urls)),``, s katero bi vključili tudi administrativni vmesnik. Celotna datoteka bi torej zgledala nekako tako: ::

    from django.conf.urls.defaults import patterns, include, url

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        (r'^articles/(\d{4})/$', 'news.views.year_archive'),
        (r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
        (r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )
    
Kaj dejansko pomenijo ti URL-ji in kako bi naj zgledali vaši URL-ji? Django uporablja za procesiranje URL strukture regularne izraze, ki vam dajajo izredno moč in natančnost pri specificiranju kaj želimo sprejeti in v kakšni obliki, vsakršne deviacije pa bi se končale z izjemo.

Tako v prvem primeru zahteveka na ``articles/2010/``, za procesiranje le-tega uporabimo funkcijo ``news.views.year_archive``, med tem ko bi v primeru zahtevka na ``articles/2010/09/`` uporabili funkcijo ``news.views.month_archive``.
    
View
----

Vsak *view* ali funkcija, s katero obdelujemo podatke, mora izpolniti eno od dveh zahtev - ali vrne HttpResponse objekt, ki vsebuje vsebino strani, ali pa vrne eno izmed izjem (i.t. Exception), vse ostalo procesiranje pa je v vaših rokah.

V našem primeru prej obstoječih URL-jev, bi lahko prikazali letni arhiv, ki smo ga zahtevali z zahtevkom na ``articles/2010/`` v sledeči obliki: ::
    
    def year_archive(request, year):
        a_list = Article.objects.filter(pub_date__year=year)
        return render_to_response('news/year_archive.html', {'year': year, 'article_list': a_list})
        
``render_to_response`` je v našem primeru ena izmed mnogih bližnjic, ki jih ima Django že vgrajene zato da nam olajša in pohitri razvoj. ``render_to_response``-u podamo samo ime predloge, ki jo bomo uporabili za izris in vrednosti spremenljivk, ki jih naša predloga pričakuje, Django pa bo opravil vse ostalo.

Nam tako preostaja le še...

Template
--------

Tako nam ostane le še izris iz podatkovne baze pridobljene vsebine. ::

    {% extends "base.html" %}

    {% block title %}Articles for {{ year }}{% endblock %}

    {% block content %}
    <h1>Articles for {{ year }}</h1>

    {% for article in article_list %}
        <p>{{ article.headline }}</p>
        <p>By {{ article.reporter.full_name }}</p>
        <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
    {% endfor %}
    {% endblock %}
    
Spremenljivke so obdane z dvojnimi zavitimi oklepaji, pri čemer lahko z isto sintakso kot v ukazni vrstici tudi tokrat dostopamo do objektovih atributov (``{{ article.headline }}``). Z to notacijo pa lahko izvajamo tudi klice na funkcije, dostopamo do ključev v slovarju (``dict``) in mest v slovarju.

``{{ article.pub_date|date:"F j, Y" }}`` uporablja t.i. *template filter*, ki uporablja Unix-ovo *pipe* notacijo, z njim pa lahko filtrirate dobljeno vrednost - v tem primeru ``datetime`` objekt pretvorimo v lepšo in bolj berljivo obliko. 

Omeniti velja še bloke. Django uporablja sistem dedovanja predlog, pri čemer definiramo neko osnovo, v kateri določimo željene bloke, ki jih lahko potem predloge, ki dedujejo osnovo, zamenjajo s svojo vsebino. 

V našem primeru bi lahko osnova ``base.html`` izgledala takole: ::

    <html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        <img src="sitelogo.gif" alt="Logo" />
        {% block content %}{% endblock %}
    </body>
    </html>

V naši prvotni predlogi smo tako prepisali naslov in glavno vsebino, nismo pa potrebovali ponovno pisati HTML značk za glavo in telo dokumenta.

Kljub temu, da se morda na tej točki zdi, da so vse te komponente močno integrirane med seboj, vas nič ne ustavlja, da ne bi uporabili neko drugo tehnologijo za dostop do podatkovne baze (npr. `SQLAlchemy <http://www.sqlalchemy.org/>`_) ali kakšen sistem za izrisovanje predlog. Vsak sistem je namreč ločen od ostalih in ne vsebuje medsebojnih odvisnosti.