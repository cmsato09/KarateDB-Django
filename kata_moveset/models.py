from django.db import models


class Kata(models.Model):

    class Series(models.Choices):
        # more to add
        HEIAN = 'Heian'
        TEKKI = 'Tekki'
        BASSAI = 'Bassai'
        KANKU = 'Kanku'

    name = models.CharField(max_length=30)
    series = models.CharField(max_length=30, choices=Series.choices)
    hiragana = models.CharField(max_length=20) # Does CharField take utf-8 characters?
    kanji = models.CharField(max_length=10)


class Stances(models.Model):
    stance_name = models.CharField(max_length=30)
    description = models.TextField()
    hiragana = models.CharField(max_length=20)
    kanji = models.CharField(max_length=10)


class Move(models.Model):

    class Direction(models.TextChoices):
        NORTH = 'N', 'North'
        SOUTH = 'S', 'South'
        EAST = 'E', 'East'
        WEST = 'W', 'West'
        NORTHEAST = 'NE', 'Northeast'
        NORTHWEST = 'NW', 'Northwest'
        SOUTHEAST = 'SE', 'Southeast'
        SOUTHWEST = 'SW', 'Southwest'

    class Leadfoot(models.TextChoices):
        RIGHT = 'R', 'right'
        LEFT = 'L', 'left'
        NEITHER = 'N', 'neither'

    class Hips(models.TextChoices):
        SHOMEN = 'S', 'shomen'
        HANMI = 'H', 'hanmi'
        GYAKUHANMI = 'G', 'gyakuhanmi'
        NEITHER = 'N', 'neither'

    class Activeside(models.TextChoices):
        RIGHT = 'R', 'right'
        LEFT = 'L', 'left'
        NEITHER = 'N', 'neither'
        BOTH = 'B', 'both'

    class Speed(models.TextChoices):
        FAST = 'F', 'fast'
        SLOW = 'S', 'slow'

    class SnapThrust(models.TextChoices):
        SNAP = 'S', 'snap'
        THRUST = 'T', 'thrust'

    class Breathing(models.TextChoices):
        IN = 'I', 'in'
        OUT = 'O', 'out'
        INOUT = 'IO', 'in-out'
        OUTIN = 'OI', 'out-in'

    kata_id = models.ForeignKey(Kata)
    move_number = models.IntegerField()
    stance = models.ForeignKey(Stances)
    direction = models.CharField(max_length=2, choices=Direction.choices)
    lead_foot = models.CharField(max_length=1, choices=Leadfoot.choices)
    hip = models.CharField(max_length=1, choices=Hips.choices)
    active_side = models.CharField(max_length=1, choices=Activeside.choices)
    speed = models.CharField(max_length=1, choices=Speed.choices)
    snapthrust = models.CharField(max_length=1, choices=SnapThrust.choices)
    interm_move = models.BooleanField()
    breath = models.CharField(max_length=2, choices=Breathing.choices)
    kiai = models.BooleanField()


class Technique(models.Model):

    class TechType(models.TextChoices):
        PUNCH = 'P', 'punch'
        Blocking = 'B', 'block'
        KICK = 'K', 'kick'
        STRIKE = 'S', 'strike'
        PREP = 'P', 'prep'
        OTHER = 'O', 'other'

    technique_name = models.CharField(max_length=30)
    description = models.TextField()
    hiragana = models.CharField(max_length=20)
    kanji = models.CharField(max_length=10)


class TechniqueToMove(models.Model):
    """
    Many-to-Many association table between Technique and Move
    """

    class Level(models.TextChoices):
        JODAN = 'J', 'jodan'
        CHUDAN = 'C', 'chudan'
        GEDAN = 'G', 'gedan'
        OTHER = 'O', 'other'

    move_id = models.ForeignKey(Move)
    technique_id = models.ForeignKey(Technique)
    level = models.CharField(max_length=1, choices=Level.choices)
