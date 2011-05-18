#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import tvdb_api
from django.core.management.base import BaseCommand
from django.db import transaction

from tvseries.series.models import Serie, Episode


series_list = ['House', 'Lost', 'Supernatural', '24', 'Battlestar Galactica', 'How not to live your life', 'The big bang theory', 'Two and a half men', 'The Office', 'How I met your mother', 'Firefly', 'Futurama', 'Stargate', 'Star Trek', 'Heroes', 'Coupling', 'South Park', 'Prison Break', 'Nikita', 'Desperate Housewives']


class Command(BaseCommand):
    args = ''
    help = 'Downloads latest series data from thetvdb.com'

    def handle(self, *args, **options):
        t = tvdb_api.Tvdb()
        # get list of all series
        for serie in series_list:
            print "importing %r" % serie
            with transaction.commit_on_success():
                s = t[serie]
                ser = Serie(
                    id=s['id'],
                    name=s['seriesname'],
                        imdb_id=s['imdb_id'][2:] if s['imdb_id'] and len(s['imdb_id']) > 3 else None,
                    rating=s['rating'],
                    poster=s['fanart']
                )
                for season in s:
                    for episode in s[season]:
                        e = s[season][episode]
                        if not e['episodename']:
                            continue
                        ep = Episode(
                            id=e['id'],
                            name=e['episodename'],
                            imdb_id=e['imdb_id'][2:] if e['imdb_id'] and len(e['imdb_id']) > 3 else None,
                            rating=e['rating'] or None,
                            episode_number=e['episodenumber'],
                            season_number=e['seasonnumber'],
                            airdate=datetime.datetime.strptime(e['firstaired'] or '2001-01-01', '%Y-%m-%d'),
                            serie=ser,
                        )
                        ep.save()
                        ser.save()
