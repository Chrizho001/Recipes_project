from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Dish(models.Model):
    title = models.CharField(max_length=30)
    average_rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='recipe', blank=False, null=False)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.title