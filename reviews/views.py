from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    review = Review.objects.order_by("-pk")

    context = {
        "review": review,
    }

    return render(request, "reviews/index.html", context)


@login_required
def create(request):

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


def detail(request, pk):

    review = Review.objects.get(pk=pk)

    comment_form = CommentForm()

    context = {
        "review": review,
        "comment_form": comment_form,
    }

    return render(request, "reviews/detail.html", context)


def delete(request, pk):

    review = Review.objects.get(pk=pk)

    review.delete()

    return redirect("reviews:index")


@login_required
def update(request, pk):

    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
        "review": review,
    }
    return render(request, "reviews/update.html", context)
