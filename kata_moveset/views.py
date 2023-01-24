import csv
import io

from django.shortcuts import render
from django.http import HttpResponse
from .models import Kata, Move, Stance, Technique, TechniqueToMove


def home_page(request):
    return HttpResponse('<html><title>Karate Kata Database</title>'
                        '<h1>Hello World!</h1>'
                        '</html>')


def upload_kata_file(request):

    if request.method == "POST":
        # User uploads csv file which contains the moveset for a specific kata
        # specified by the user (kata_id_value)
        kata_id = int(request.POST["kata_upload_choice"])
        kata_obj = Kata.objects.get(id=kata_id)

        stances = {
            stance.stance_initial: stance
            for stance in Stance.objects.all()
        }
        speeds = {entry.label: entry.value for entry in Move.Speed}
        levels = {entry.label: entry.value for entry in TechniqueToMove.Level}

        csv_file = request.FILES['uploadKataCSV']
        data_set = csv_file.read().decode('utf-8-sig')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string)

        for entry in reader:
            move = Move.objects.create(
                kata_id=kata_obj,
                move_number=entry['Move #'],
                stance=stances[entry['stance']],
                direction=entry['direction'],
                lead_foot=entry['lead foot'],
                hip=entry['hips'],
                active_side=entry['active side'],
                speed=speeds[entry['speed']],
                snapthrust=entry['snap/thrust'],
                interm_move=entry['interm move'] == 'Y',
                breath=entry['breath'],
                kiai=bool(entry['kiai']),
            )

            technique = Technique.objects.get(
                technique_name__iexact=entry['tech subtype'])

            levels_of_tech = entry["level of tech"].split("+")
            for level in levels_of_tech:
                TechniqueToMove.objects.create(
                    move_id=move,
                    technique_id=technique,
                    level=levels[level]
                )

    context = {
        'kata_choices': Kata.objects.all(),
    }

    return render(request, 'upload-kata.html', context)
