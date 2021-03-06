Model-Template-View
===========================================

Django sledi tako imenovani `Model-View-Controller <http://en.wikipedia.org/wiki/Model–view–controller>`_ filozofiji, kar pomeni, da so aplikacije zasnovane tako, da imamo čisto ločitev podatkovne baze (*Model*), aplikativne logike (*Controller*) in izrisovalnih predlog (*View*). To pomaga ohranjati kodo čisto in brez grdih *hackov* in predloge brez aplikativne logike (in posledično veliko bolj prijazne očem oblikovalcev).

Striktno gledano se Django opredeljuje kot MTV oz. Model-Template-View, pri čemer Template služi kot View in View kot kontroler. Takšno poimenovanje se uporablja tudi v Django-tovi dokumentaciji in ker je za vse praktične namene ekvivalentno MVC, bomo za namene zmanjšanja zmešnjave ob obračanju na uradno dokumentacijo sledili Django-tovemu poimenovanju.

Bojni načrt
-----------

Odločili smo se, da potrebuje naša spletna stran, ki je do te točke bila le preprosta vizitka tudi možnost objavljanja člankov in novic, ki bodo v pomoč našim strankam, zatorej bomo za začetno predstavitev konceptov Django-ta in njegove infrastrukture zgradili preprosto novičkarsko aplikacijo.  
