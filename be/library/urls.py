from django.urls import path
from .views import (
    index,
    library,
    book_detail,
    track_reading_progress,
    login_view,
    register_view,
    logout_view,
    about,
    add_book,
    wishlist,
    add_to_wishlist,
    goals,
    account,
    delete_account,
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("library/", library, name="library"),
    path("goals/", goals, name="goals"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
    path(
        "book/<int:book_id>/track/",
        track_reading_progress,
        name="track_reading_progress",
    ),
    path("about/", about, name="about"),
    path("add/", add_book, name="add"),
    path("addtowishlist/<int:book_id>/", add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", wishlist, name="wishlist"),
    path("account/", account, name="account"),
    path("delete_account/", delete_account, name="delete_account"),
]
