from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    rating = models.IntegerField(
        null=True, blank=True, choices=[(i, i) for i in range(1, 6)]
    )
    cover_image = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    pages_read = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.book.title} ({self.pages_read} pages read)"
        )


class Wishlist(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="reading_list"
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Reading List - {self.book.title}"
