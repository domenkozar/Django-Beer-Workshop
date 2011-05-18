from django.db import models


# naming after original structure?
# i18n
class Episode(models.Model):
    name = models.CharField(max_length=240)
    imdb_id = models.IntegerField('', blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    episode_number = models.IntegerField()
    season_number = models.IntegerField()
    airdate = models.DateTimeField() # timezone? l10n?

    serie = models.ForeignKey('Serie')


class Serie(models.Model):
    name = models.CharField(max_length=240)
    imdb_id = models.IntegerField('', blank=True, null=True)
    rating = models.FloatField()
    poster = models.ImageField(upload_to="series")

# vse kar ni blo casa obdelat, se lahko nauci na kiberpipa - intranet
