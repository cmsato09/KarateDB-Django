import csv

from django.shortcuts import render
from django.http import HttpResponse
from .models import Kata, Move


def home_page(request):
    return HttpResponse('<html><title>Karate Kata Database</title>'
                        '<h1>Hello World!</h1>'
                        '</html>')


def upload_kata_file(request):
    kata_choices = Kata.objects.all

    if request.method == "POST":
        kata_id_value: int = request.POST.get("kata_upload_choice")
        csv_file = request.FILES['uploadKataCSV']
        data_set = csv_file.read()
        reader = csv.DictReader(data_set)

        for entry in reader:
            Move.objects.create(
                kata_id=kata_id_value,
                move_number=entry['Move #'],
                stance=entry['stance'],
                direction=entry['direction'],
                lead_foot=entry['lead foot'],
                hip=entry['hips'],
                active_side=entry['active side'],
                speed=entry['speed'],
                snapthrust=entry['snap/thrust'],
                interm_move=True if entry['interm move'] == 'Y' else False,
                breath=entry['breath'],
                kiai=True if entry['kiai'] else False,
            )

    return render(request, 'upload-kata.html', {'kata_choices': kata_choices})
