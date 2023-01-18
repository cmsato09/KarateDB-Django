# Generated by Django 4.1.5 on 2023-01-18 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kata_moveset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stance_name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='')),
                ('hiragana', models.CharField(max_length=20)),
                ('kanji', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='technique',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='move',
            name='stance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kata_moveset.stance'),
        ),
        migrations.DeleteModel(
            name='Stances',
        ),
    ]