from django.db import models


class Kata(models.Model):

    class Series(models.TextChoices):
        HEIAN = 'Heian'
        TEKKI = 'Tekki'
        BASSAI = 'Bassai'
        KANKU = 'Kanku'
        OTHER = 'Other'

    name = models.CharField(max_length=30, unique=True)
    series = models.CharField(max_length=30, choices=Series.choices)
    hiragana = models.CharField(max_length=20)
    kanji = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Stance(models.Model):
    stance_name = models.CharField(max_length=30, unique=True)
    stance_initial = models.CharField(max_length=1, default='')
    description = models.TextField(blank=True, default='')
    hiragana = models.CharField(max_length=20)
    kanji = models.CharField(max_length=10)

    def __str__(self):
        return self.stance_name


class Technique(models.Model):

    class TechType(models.TextChoices):
        PUNCH = 'PU', 'punch'
        Blocking = 'B', 'block'
        KICK = 'K', 'kick'
        STRIKE = 'S', 'strike'
        PREP = 'PR', 'prep'
        OTHER = 'O', 'other'

    technique_name = models.CharField(max_length=30, unique=True)
    technique_type = models.CharField(max_length=10, choices=TechType.choices,
                                      default='O')
    description = models.TextField(blank=True, default='')
    hiragana = models.CharField(max_length=20)
    kanji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.technique_name}"


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

    kata_id = models.ForeignKey(Kata, on_delete=models.CASCADE)
    move_number = models.IntegerField()
    technique = models.ManyToManyField(Technique, through='TechniquetoMove')
    stance = models.ForeignKey(Stance, on_delete=models.CASCADE)
    direction = models.CharField(max_length=2, choices=Direction.choices)
    lead_foot = models.CharField(max_length=1, choices=Leadfoot.choices)
    hip = models.CharField(max_length=1, choices=Hips.choices)
    active_side = models.CharField(max_length=1, choices=Activeside.choices)
    speed = models.CharField(max_length=1, choices=Speed.choices)
    snapthrust = models.CharField(max_length=1, choices=SnapThrust.choices)
    interm_move = models.BooleanField()
    breath = models.CharField(max_length=2, choices=Breathing.choices)
    kiai = models.BooleanField()

    def __str__(self):
        return f"{self.kata_id.name} {self.move_number} " \
               f"{self.get_all_techniques_per_move()}"

    def get_all_techniques_per_move(self):
        return " + ".join([tech.technique_name for tech in self.technique.all()])


class TechniqueToMove(models.Model):
    """
    Many-to-Many association table between Technique and Move
    """

    class Level(models.TextChoices):
        JODAN = 'J', 'jodan'
        CHUDAN = 'C', 'chudan'
        GEDAN = 'G', 'gedan'
        OTHER = 'O', 'other'

    move_id = models.ForeignKey(Move, on_delete=models.CASCADE)
    technique_id = models.ForeignKey(Technique, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=Level.choices)

    def __str__(self):
        return f"{self.move_id.kata_id.name} {self.move_id.move_number} " \
               f"{self.technique_id.technique_name} {self.level}"

    def get_kata_name_and_move_num(self):
        return f"{self.move_id.kata_id.name} {self.move_id.move_number}"
