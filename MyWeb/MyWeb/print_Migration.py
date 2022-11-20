import os
from sys import stdout
import django
from io import StringIO
from django.core.management import call_command
from django.apps import apps
import re

os.environ['DJANGO_COLORS'] = 'nocolor'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'settings')

django.setup()

out = StringIO()

call_command('showmigrations', '-p', stdout=out)

migrations = [line.strip() for line in out.getvalue().split('\n')]

migrations_regex = re.compile('^\[[X ]\]  ([^.]*).(.*)$')

with open('source_migration.sql', 'w') as out_file:
    for m in migrations:
        searched_migration = re.search(migrations_regex, m)
        if searched_migration:
            app_name = searched_migration.group(1)
            migration_name = searched_migration.group(2)
            app_path = apps.get_app_config(app_name).module.__file__
            call_command('sqlmigrate', app_name,
                         migration_name, stdout=out_file)
