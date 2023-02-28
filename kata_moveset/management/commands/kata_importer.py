import csv

from django.core.management.base import BaseCommand, CommandError
from kata_moveset.models import Kata


class Command(BaseCommand):
    help = 'Imports kata starter data into the database'

    def handle(self, *args, **options):
        kata_csv_file = 'kata_moveset/csvfiles/karate_kata.csv'
        with open(kata_csv_file, encoding="utf-8-sig") as kata_csv:
            reader = csv.DictReader(kata_csv)
            for entry in reader:
                Kata.objects.create(
                    name=entry['name'],
                    series=entry['series'],
                    hiragana=entry['hiragana'],
                    kanji=entry['kanji'])
