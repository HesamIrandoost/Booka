from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="reviews"
    )
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    subject = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    star = models.IntegerField(
        default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject[:10]}"


class ReviewLike(models.Model):
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="review_likes"
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review_likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "review"], name="unique_review_like"
            )
        ]

    def __str__(self):
        return f"{self.user_id} likes {self.review_id}"


class Collection(models.Model):
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="collections"
    )
    books = models.ManyToManyField("Book", related_name="collections", blank=True)
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to="collections/covers/", blank=True, null=True)
    description = models.TextField(default="My Collection", blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:10]
