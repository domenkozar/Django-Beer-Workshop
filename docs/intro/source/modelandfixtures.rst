Model in fixtures
=================

Pred pisanjem samih modelov za začetek postojimo in najprej razmislimo o našem problemu. Če hočemo v našo videoteko shranjevati podatke o serijah, moramo torej shraniti podatke o seriji in njenih epizodah. To pomeni, da bomo imeli dve tabeli (eno Serie in drugo Episode).

Podatki o seriji, ki jih bomo shranili bodo unikatni identifikator, ime serije, IMDB unikatni identifikator in ocena same serije.

Vsaka epizoda, ki jo bomo shranili, bo pripadala eni seriji, kar pomeni da bomo morali ustvariti še 1:N relacijo v podatkovni bazi, poleg tega pa bomo shranili še ime, IMDB identifikator, oceno, številko epizode, številko serije in datum prvega predvajanja. 

Modela bosta torej izgledala tako:

...

Pred uvozom podatkov moramo seveda še ustvariti podatkovno bazo, v katero bomo shranjevali podatke. Da to storimo, moramo slediti več korakom.

