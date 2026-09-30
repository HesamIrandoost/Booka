from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to="authors/profiles/")
    biography = models.TextField()
    website = models.URLField(max_length=300, blank=True, null=True)
    date_born = models.DateField(auto_now=False, auto_now_add=False)
    place_born = models.CharField(max_length=250)

    slug = models.SlugField(blank=True, unique=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def born(self):
        return f"{self.place_born}, {self.date_born}"

    """
    def save(self, *args, **kwargs):
        if not self.slug:
            fslug = slugify(self.first_name)
            lslug = slugify(self.last_name)
            flslug = f"{fslug} {lslug} {self.pk}"
            self.slug = slugify(flslug)
        super().save(*args, **kwargs)
    """

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
