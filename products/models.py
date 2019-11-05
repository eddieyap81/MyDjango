from django.db import models
from django.urls import reverse

# Create your models here.
class Chair(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
                    #blank=True means not required
                    #null=True means db can have null values
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
                    #blank=False means required
                    #null=False means db can't have null values
    featured    = models.BooleanField(default=False) #null=True, default=True

    def get_absolute_url(self):
        return reverse("products:chair-detail",kwargs={"my_id": self.id}) #f"/products/{self.id}"

class Table(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default="This is cool!")
