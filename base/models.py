from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


score_validators = [MinValueValidator(0), MaxValueValidator(10)]

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    write = models.IntegerField(
        validators=score_validators, null=True, blank=True
    )
    listen = models.IntegerField(
        validators=score_validators, null=True, blank=True
    )
    speak = models.IntegerField(
        validators=score_validators, null=True, blank=True
    )
    score = models.FloatField()
    fulfilled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.score = round((self.speak + self.write + self.listen) / 3, 2)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["fulfilled"]
