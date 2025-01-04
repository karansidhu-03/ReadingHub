from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, ReadingProgress, UserProfile, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse


def index(request):
    books = Book.objects.all()
    return render(request, "library/index.html", {"books": books})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
    return redirect("index")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            return JsonResponse(
                {"success": False, "error": "Passwords do not match."}, status=400
            )
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            login(request, user)
            messages.success(request, "Registered successfully")
            return redirect("index")
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return redirect("index")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("index")


def library(request):
    books = Book.objects.all()
    return render(request, "library/library.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "library/book_detail.html", {"book": book})


@login_required
def track_reading_progress(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        pages_read = request.POST.get("pages_read")
        if pages_read.isdigit():
            pages_read = int(pages_read)
            user_profile = UserProfile.objects.get(user=request.user)
            ReadingProgress.objects.create(
                user=user_profile.user, book=book, pages_read=pages_read
            )
            return redirect("book_detail", book_id=book.id)

    return render(request, "library/reading_progress.html", {"book": book})


@login_required
def add_to_wishlist(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, id=book_id)
        # Assuming you have a Wishlist model and a user is logged in
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user, book=book
        )
        if created:
            # Optionally, you can add a success message here
            messages.success(request, f"{book.title} has been added to your wishlist.")
        else:
            messages.info(request, f"{book.title} is already in your wishlist.")

        return redirect("book_detail", book_id=book.id)


def wishlist(request):
    return render(request, "library/wishlist.html")


def about(request):
    return render(request, "library/about.html")


def goals(request):
    return render(request, "library/goal.html")


def account(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username")
        bio = request.POST.get("bio")
        password = request.POST.get("password")

        if username:
            user.username = username
            user.save()

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.bio = bio
        user_profile.save()

        if password:
            user.set_password(password)
            user.save()
            messages.success(
                request, "Your password has been changed. Please log in again."
            )
            return redirect("login")

        messages.success(request, "Your profile has been updated.")
        return redirect("account")
    return render(request, "library/account.html")


def add_book(request):
    ratings = list(range(1, 6))
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        publication_date = request.POST.get("publication_date")
        rating = request.POST.get("rating")
        cover_image = request.POST.get("cover_image")

        new_book = Book(
            title=title,
            description=description,
            author=author,
            genre=genre,
            publication_date=publication_date,
            rating=rating,
            cover_image=cover_image,
        )

        new_book.save()

        return redirect("/")

    return render(request, "library/add_book.html", {"ratings": ratings})


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("index")
