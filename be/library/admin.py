from django.contrib import admin
from .models import Book, UserProfile, ReadingProgress, Wishlist

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(ReadingProgress)
admin.site.register(Wishlist)
