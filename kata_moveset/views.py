import csv
import io

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Kata, Move, Stance, Technique, TechniqueToMove


def home_page(request):
    return HttpResponse('<html><title>Karate Kata Database</title>'
                        '<h1>Hello World!</h1>'
                        '</html>')


def upload_kata_file(request):
    if request.method == "POST":
        kata_id = int(request.POST["kata_upload_choice"])
        kata_obj = Kata.objects.get(id=kata_id)

        stances = {
            stance.stance_initial: stance
            for stance in Stance.objects.all()
        }
        speeds = {entry.label: entry.value for entry in Move.Speed}
        levels = {entry.label: entry.value for entry in TechniqueToMove.Level}

        csv_file = request.FILES['uploadKataCSV']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string)

        # moves = []
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

            # TODO: import script normalize by importing lowercase
            technique = Technique.objects.get(
                technique_name__iexact=entry['tech subtype'])

            levels_of_tech = entry["level of tech"].split("+")
            for level in levels_of_tech:
                TechniqueToMove.objects.create(
                    move_id=move,
                    technique_id=technique,
                    level=levels[level]
                )

            # moves.append(move)
        # Move.objects.bulk_create(moves)

        messages.success(request, "Successfully uploaded move data")
        return redirect("KataDB:upload-kata-csvfile")  # TODO: go somewhere else

    context = {
        'kata_choices': Kata.objects.all(),
    }
    return render(request, 'upload-kata.html', context)
