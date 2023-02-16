import csv
import io
import django_filters
import django_tables2 as tables

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django_filters.views import FilterView
from .models import Kata, Move, Stance, Technique, TechniqueToMove


def home_page(request):
    return render(request, 'home.html')


def upload_kata_file(request):

    if request.method == "POST":
        # User uploads csv file which contains the moveset for a specific kata
        # specified by the user (kata_post_id)
        kata_post_id = int(request.POST["kata_upload_choice"])
        kata_obj = Kata.objects.get(id=kata_post_id)

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

            # Many-to-Many TechniquetoMove entry set-up
            wazas = [tech.title() for tech in entry['tech subtype'].split("+")]
            techniques = Technique.objects.filter(
                technique_name__in=wazas)

            levels_of_tech = entry['level of tech'].split("+")

            for tech, level in zip(techniques, levels_of_tech):
                TechniqueToMove.objects.create(
                    move_id=move,
                    technique_id=tech,
                    level=levels[level]
                )
        messages.success(request, "Successfully uploaded CSV file")
        return HttpResponseRedirect("")

    context = {
        'kata_choices': Kata.objects.all(),
    }

    return render(request, 'upload-kata.html', context)


class MoveSetTable(tables.Table):
    class Meta:
        model = Move
        template_name = "django_tables2/bootstrap.html"
        fields = ('kata_id', 'move_number', 'technique', 'stance', 'direction',
                  'lead_foot', 'hip', 'active_side', 'speed', 'snapthrust',
                  'interm_move', 'breath', 'kiai')


# class KataTableView(tables.SingleTableView):
#     model = Move
#     table_class = MoveSetTable
#     template_name = 'kata-table.html'

class KataFilter(django_filters.FilterSet):

    class Meta:
        model = Move
        fields = ['kata_id', 'technique', 'stance', 'lead_foot', 'hip']


class KataTableFilter(tables.SingleTableMixin, FilterView):
    model = Move
    table_class = MoveSetTable
    template_name = 'kata-table.html'

    filterset_class = KataFilter
