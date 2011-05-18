#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tvdb_api
from django.core.management.base import BaseCommand, CommandError
from django.db import models, transaction

from tvseries.series.models import Serie, Episode



class Command(BaseCommand):
    args = ''
    help = 'Downloads latest series data from thetvdb.com'

    def handle(self, *args, **options):
        t = tvdb_api.Tvdb()
        # get list of all series
        for serie in series_list:
            with transaction.commit_on_success():
                s = t[serie]
                Serie()
                for episode in s.episodes:
                    Episode()
