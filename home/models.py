from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )
    userroutineID = models.ForeignKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_userroutineID",
    )
    routinesID = models.BigIntegerField(
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_user",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    user = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="homepage_user",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Routines(models.Model):
    "Generated Model"
    routineID = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        related_name="routines_routineID",
    )
    routine = models.BigIntegerField()
    description = models.BigIntegerField()
    idh = models.ForeignKey(
        "home.Routinesexcercise",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="routines_idh",
    )


class Routinesexcercise(models.Model):
    "Generated Model"
    routineexcerciseID = models.ForeignKey(
        "home.HomePage",
        on_delete=models.CASCADE,
        related_name="routinesexcercise_routineexcerciseID",
    )
    routines = models.BigIntegerField()
    excercise = models.BigIntegerField()
    routineID = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Excercise(models.Model):
    "Generated Model"
    excerciseID = models.ForeignKey(
        "home.Routinesexcercise",
        on_delete=models.CASCADE,
        related_name="excercise_excerciseID",
    )
