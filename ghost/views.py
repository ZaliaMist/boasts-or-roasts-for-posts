from django.shortcuts import render, redirect
from ghost.models import ModelForBoastsAndRoasts
from ghost.forms import FormForBoastsAndRoasts

def home_view(request):
    posts = ModelForBoastsAndRoasts.objects.all().order_by('-time')
    return render(request, 'home.html', {'posts': posts}, greeting="Homepage")


def boasts_view(request):
    all_posts = ModelForBoastsAndRoasts.objects.all().order_by('-time')
    stores_post_content = []
    for arr_index in all_posts:
        if arr_index.boast is True:
            stores_post_content.append(arr_index)
    return render(
        request, 'home.html',
        {'posts': stores_post_content}
        )


def roasts_view(request):
    all_posts = ModelForBoastsAndRoasts.objects.all().order_by('-time')
    stores_post_content = []
    for arr_index in all_posts:
        if arr_index.boast is False:
            stores_post_content.append(arr_index)
    return render(
        request, 'home.html',
        {'posts': stores_post_content}
        )


def create_post_view(request):
    if request.method == "POST":
        form = FormForBoastsAndRoasts(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ModelForBoastsAndRoasts.objects.create(
                body=data["body"], boast=data["boast"]
            )
            return redirect("/")
    form = FormForBoastsAndRoasts()
    return render(request, 'createpost.html', {"form": form})

def sort_by_view(request):
    posts = ModelForBoastsAndRoasts.objects.all().order_by('-vote_holder')
    return render(request, 'home.html', {'posts': posts})


def like_view(request, post_id):
    post = ModelForBoastsAndRoasts.objects.get(id=post_id)
    post.up_votes += 1
    post.vote_holder += 1
    post.save()
    return redirect("home")


def dislike_view(request, post_id):
    post = ModelForBoastsAndRoasts.objects.get(id=post_id)
    post.down_votes += 1
    post.vote_holder -= 1
    post.save()
    return redirect("home")

