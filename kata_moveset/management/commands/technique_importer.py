import csv

from django.core.management.base import BaseCommand, CommandError
from kata_moveset.models import Technique


class Command(BaseCommand):
    help = 'Imports Technique starter data into the database'

    def handle(self, *args, **options):
        tech_csv_file = 'kata_moveset/csvfiles/karate_technique.csv'
        with open(tech_csv_file, encoding="utf-8-sig") as tech_csv:
            reader = csv.DictReader(tech_csv)
            for entry in reader:
                Technique.objects.create(
                    technique_name=entry['name'],
                    technique_type=entry['type'],
                    hiragana=entry['hiragana'],
                    kanji=entry['kanji'])
