from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='authors/profiles/', blank=True, null=True)
    biography = models.TextField()
    website = models.URLField(max_length=300, blank=True,null=True)
    date_born = models.DateField(auto_now=False, auto_now_add=False)
    place_born = models.CharField(max_length=250) 

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def born(self):
        return f"{self.place_born}, {self.date_born}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"