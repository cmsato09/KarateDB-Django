import csv

from django.core.management.base import BaseCommand, CommandError
from kata_moveset.models import Stance


class Command(BaseCommand):
    help = 'Imports kata starter data into the database'

    def handle(self, *args, **options):
        stance_csv_file = 'kata_moveset/csvfiles/karate_stances.csv'
        with open(stance_csv_file, encoding="utf-8-sig") as stance_csv:
            reader = csv.DictReader(stance_csv)
            for entry in reader:
                Stance.objects.create(
                    stance_name=entry['name'],
                    stance_initial=entry['initial'],
                    hiragana=entry['hiragana'],
                    kanji=entry['kanji'])
