import uuid as uuid
from django.db import models

RACE_KINDS = (
    ("team", "Team"),
    ("men", "Men"),
    ("women", "Women"),
    ("other", "Other"),
)


class Tournament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Race(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    fis_id = models.PositiveIntegerField(default=0)
    place = models.CharField(max_length=50)
    tournament = models.ForeignKey("Tournament", related_name="races", on_delete=models.CASCADE)
    date = models.DateTimeField()
    kind = models.CharField(max_length=50, choices=RACE_KINDS)
    hill_size = models.CharField(max_length=10)
    details = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.place} {self.hill_size} {self.date.strftime('%Y-%m-%d')}{' details' if self.details else ''}"


class Jumper(models.Model):
    fis_code = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    born = models.PositiveIntegerField(null=True, blank=True)
    nation = models.ForeignKey("Country", related_name="jumpers", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):

    class Meta:
        verbose_name_plural = "Countries"

    fis_code = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Jump(models.Model):
    distance = models.FloatField()
    distance_points = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    judge_a = models.FloatField(null=True, blank=True)
    judge_b = models.FloatField(null=True, blank=True)
    judge_c = models.FloatField(null=True, blank=True)
    judge_d = models.FloatField(null=True, blank=True)
    judge_e = models.FloatField(null=True, blank=True)
    judge_points = models.FloatField(null=True, blank=True)
    gate = models.IntegerField(null=True, blank=True)
    gate_points = models.FloatField(null=True, blank=True)
    wind = models.FloatField(null=True, blank=True)
    wind_points = models.FloatField(null=True, blank=True)
    total_points = models.FloatField()
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.distance}, {self.total_points}"


class Participant(models.Model):
    rank = models.PositiveIntegerField(null=True, blank=True)
    bib = models.PositiveIntegerField(null=True, blank=True)
    jumper = models.ForeignKey("Jumper", related_name="participated", on_delete=models.CASCADE)
    jump_1 = models.ForeignKey(
        "Jump",
        null=True,
        blank=True,
        related_name="first_jumps",
        on_delete=models.CASCADE
    )
    jump_2 = models.ForeignKey(
        "Jump",
        null=True,
        blank=True,
        related_name="second_jumps",
        on_delete=models.CASCADE
    )
    race = models.ForeignKey("Race", on_delete=models.CASCADE, to_field="uuid")
    total_points = models.FloatField(null=True, blank=True)
    diff = models.FloatField(null=True, blank=True)
    disqualified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.disqualified = self.rank is None and self.race.kind != "team"
        return super(Participant, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.jumper.name} {self.race.place} {self.race.date}"


class ParticipantCountry(models.Model):

    class Meta:
        verbose_name_plural = "Participant countries"

    rank = models.PositiveIntegerField(null=True, blank=True)
    country = models.ForeignKey("Country", related_name="participated_countries", on_delete=models.CASCADE)
    race = models.ForeignKey("Race", on_delete=models.CASCADE)
    total_points = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.country.name} {self.race.place} {self.race.date.strftime('%Y-%m-%d')}"
