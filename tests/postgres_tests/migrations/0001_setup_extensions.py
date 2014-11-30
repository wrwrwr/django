# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.operations import HStoreExtension, UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    vendors = [
        'postgres'
    ]

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        UnaccentExtension(),
    ]
